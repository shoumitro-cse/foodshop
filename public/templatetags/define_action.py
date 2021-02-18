import itertools
import re
from datetime import datetime

from django import template
from django.template import Context
from django.template.defaultfilters import stringfilter, linebreaksbr, urlize
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from  public.controlers import ProductData, Shopping, UserData

productData = ProductData()
shopping = Shopping()
userData = UserData()

register = template.Library()


@register.inclusion_tag('t2.html', takes_context=True)
def jump_link(context):
    context['pricing'] = "http://127.0.0.1:8000"
    context['home'] = "http://127.0.0.1:8000"
    return {
        'link': context['pricing'],
        'title': context['home'],
    }

@register.inclusion_tag('pricing.html')
def show_results():
    return "dgd"


@register.simple_tag
def my_tag(a, b, *args, **kwargs):
    warning = kwargs['warning']
    profile = kwargs['profile']
    return [a,b,args,kwargs]

register.simple_tag(lambda x: x - 1, name='minusone')

@register.simple_tag(name='minustwo')
def some_function(value):
    return value - 2

@register.simple_tag(name="get_user_email")
def get_user_email(request):
    email = userData.getSessionUserEmail(request)
    if email:
        return email
    else:
        return None

@register.simple_tag(name="get_cart_list")
def get_cart_list(request):
    email = userData.getSessionUserEmail(request)
    if email:
        user_obj = userData.getUserObj(user_email=email)
        if user_obj:
            cart_list = shopping.getCart(user_obj)
            if cart_list:
                return cart_list
            else:
                return None
    else:
        return "Not Email"

# @register.simple_tag
@register.simple_tag(name="get_addressee")
def get_addressee():
    return " World"

@register.simple_tag(name="define")
def define(val=None):
  return val

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter
@stringfilter #If you’re writing a template filter that only expects a string as the first argument, you should use the decorator stringfilter.
def lower(value):
    return value.lower()

# register.filter('cut', cut)
# register.filter('lower', lower)

@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong style='color:blue'>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)

@register.filter(needs_autoescape=True)
def urlize_and_linebreaks(text, autoescape=True):
    return linebreaksbr(
        urlize(text, autoescape=autoescape),
        autoescape=autoescape
    )

@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

# from datetime import datetime
# @register.filter
# def datetimeformat(value, format_string):
#     return datetime.strftime(value.__str__(), format_string)

# @register.simple_tag(takes_context=True)
# def current_time(context, format_string):
#     timezone = context['timezone']
#     return your_get_current_time_method(timezone, format_string)

@register.filter(expects_localtime=True)
def businesshours(value):
    try:
        return 9 <= value.hour < 17
    except AttributeError:
        return ''


class SetVarNode(template.Node):
  def __init__(self, new_val, var_name):
    self.new_val = new_val
    self.var_name = var_name

  def render(self, context):
    context[self.var_name] = self.new_val
    return ''

@register.tag
def setvar(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    print("{} tag requires arguments".format(token.contents.split()[0]))
  m = re.search(r'(.*?) as (\w+)', arg)
  if not m:
    print("{} tag had invalid arguments".format(tag_name))
  new_val, var_name = m.groups()
  if not (new_val[0] == new_val[-1] and new_val[0] in ('"', "'")):
    print("{} tag's argument should be in quotes".format(tag_name))
  return SetVarNode(new_val[1:-1], var_name)



# class CycleNode(template.Node):
#     def __init__(self, cyclevars):
#         self.cycle_iter = itertools.cycle(cyclevars)
#
#     def render(self, context):
#         return next(self.cycle_iter)


#format time
class FormatTimeNode(template.Node):
  def __init__(self, date_to_be_formatted, format_string):
    self.date_to_be_formatted = template.Variable(date_to_be_formatted)
    self.format_string = format_string

  def render(self, context):
    try:
      actual_date = self.date_to_be_formatted.resolve(context)
      return actual_date.strftime(self.format_string)
    except template.VariableDoesNotExist:
      return ''

@register.tag(name="format_time")
def do_format_time(parser, token):
  try:
    # split_contents() knows not to split quoted strings.
    tag_name, date_to_be_formatted, format_string = token.split_contents()
  except ValueError:
    raise template.TemplateSyntaxError(
      "%r tag requires exactly two arguments" % token.contents.split()[0]
    )
  if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
    raise template.TemplateSyntaxError(
      "%r tag's argument should be in quotes" % tag_name
    )
  return FormatTimeNode(date_to_be_formatted, format_string[1:-1])


# for upper case
class UpperNode(template.Node):
  def __init__(self, nodelist):
    self.nodelist = nodelist

  def render(self, context):
    output = self.nodelist.render(context)
    return output.upper()

@register.tag(name='upper')
def do_upper(parser, token):
  nodelist = parser.parse(('endupper',))
  parser.delete_first_token()
  return UpperNode(nodelist)

# for comment
class CommentNode(template.Node):
  def render(self, context):
    return ''

@register.tag(name='commenttag')
def do_commenttag(parser, token):
  nodelist = parser.parse(('endcommenttag',))
  parser.delete_first_token()
  return CommentNode()

@register.simple_tag()
def render(self, context):
    t = context.template.engine.get_template('tutorial.html')
    return t.render(Context({'var': 123}, autoescape=context.autoescape))
