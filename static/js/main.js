
$(document).ready(function () {

    let err = 0;

    $("#signin_form input[name='email']").on("keyup change blur", function () {
        let input_value = $(this).val();
        my = $(this);

        $.get("/foodshop/public/check_email/?email=" + input_value, function (data, status) {
            if (data === "False") {
//                           alert("Data: " + data + "\nStatus: " + status + "\nemail: " + input_value);
                $("#login_email_err").text("Invalid Email Address").css("display", "block");
                err = 1;
                my.css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
                my.next().css("display", "none");
                my.siblings(":last").css("display", "block");
            }
        });

        if (input_value == "") {
            $("#login_email_err").text("Email is Empty").css("display", "block");
        } else {
            $("#login_email_err").css("display", "none");

        }

        let email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;

        if (email_regex.test(input_value)) {
            $(this).css({"border-color": "#d3d3d3", "box-shadow": "none"});
            $(this).siblings(":last").css("display", "none");
            $(this).next().css("display", "block");
            err = 0;
        } else {
            err = 1;
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
            $(this).next().css("display", "none");
            $(this).siblings(":last").css("display", "block");
        }
    });

    $("#signin_form input[name='password']").on("keyup change blur", function () {
        let input_value = $(this).val();

        if (input_value == "") {
            $("#login_pass_err").text("Password is Empty").css("display", "block");
        } else {
            $("#login_pass_err").css("display", "none");

        }

//                    /^
//                        (?=.*\d)          // should contain at least one digit
//                        (?=.*[a-z])       // should contain at least one lower case
//                        (?=.*[A-Z])       // should contain at least one upper case
//                        [a-zA-Z0-9]{8,}   // should contain at least 8 from the mentioned characters
//                     $/

        let pass_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;//Example = Bd12345678

        if (pass_regex.test(input_value)) {
            $(this).css({"border-color": "#d3d3d3", "box-shadow": "none"});
            $(this).siblings(":last").css("display", "none");
            $(this).next().css("display", "block");
            err = 0;
        } else {
            err = 1;
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
            $(this).next().css("display", "none");
            $(this).siblings(":last").css("display", "block");
        }
    });


    $("#signin_form input[type='submit']").on("click", function (event) {
        event.preventDefault();

        let input_list = $("#signin_form .input_group input");
        for (var i = 0; i < input_list.length; i++) {
            if (input_list[i].value === "") {
                input_list[i].style.borderColor = "red";
                input_list[i].style.boxShadow = "-1px 0px 1px 2px red";
                $("#login_email_err").text("Email is not match").css("display", "block");
                $("#login_pass_err").text("Password is not match").css("display", "block");
                err = 1;
            } else {
//                            console.log(input_list[i].value);
//                             err = 0;
            }
        }

        if (err === 0) {
            email = $("#signin_form input[name='email']").val();
            password = $("#signin_form input[name='password']").val();
            $.get("/foodshop/public/user_check/?email=" + email + "&password=" + password, function (data, status) {
                if (data === "True") {
//                           alert("Data: " + data + "\nStatus: " + status);
                    $("#login_email_err").css("display", "none");
                    $("#login_pass_err").css("display", "none");
                    $("#invalid_user").css("display", "none");
                    $("#signin_form").submit();
                } else {
                    $("#invalid_user").text("Invalid Email or Password.").css("display", "block");
                }
            });

        } else {
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
        }
    });


//              for signUp validation
    $("#signup_form input[name='fullname']").on("keyup change blur", function () {
        let input_value = $(this).val();

        if (input_value == "") {
            $("#fulname_err").text("Fullname is Empty").css("display", "block");
        } else {
            $("#fulname_err").css("display", "none");

        }

        if (input_value.length > 3) {
            console.log(input_value.length)
            $(this).css({"border-color": "#d3d3d3", "box-shadow": "none"});
            $(this).siblings(":last").css("display", "none");
            $(this).next().css("display", "block");
            err = 0;
        } else {
            err = 1;
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
            $(this).next().css("display", "none");
            $(this).siblings(":last").css("display", "block");
        }
    });

    $("#signup_form input[name='email']").on("keyup change blur", function () {
        let input_value = $(this).val();
        let my = $(this);
        $.get("/foodshop/public/check_email/?email=" + input_value, function (data, status) {
            if (data === "True") {
//                           alert("Data: " + data + "\nStatus: " + status + "\nemail: " + input_value);
                $("#email_err").text("Email already exists").css("display", "block");
                err = 1;
                my.css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
                my.next().css("display", "none");
                my.siblings(":last").css("display", "block");
            }
        });

        if (input_value == "") {
            $("#email_err").text("Email is Empty").css("display", "block");
        } else {
            $("#email_err").css("display", "none");
        }

        let email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;

        if (email_regex.test(input_value)) {
            $(this).css({"border-color": "#d3d3d3", "box-shadow": "none"});
            $(this).siblings(":last").css("display", "none");
            $(this).next().css("display", "block");
            err = 0;
        } else {
            err = 1;
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
            $(this).next().css("display", "none");
            $(this).siblings(":last").css("display", "block");
        }
    });

    $("#signup_form input[name='password']").on("keyup change blur", function () {
        let input_value = $(this).val();
        if (input_value == "") {
            $("#signup_pass_err").text("Password is Empty").css("display", "block");
        } else {
            $("#signup_pass_err").css("display", "none");

        }
        let pass_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;//Example = Bd12345678

        if (pass_regex.test(input_value)) {
            $(this).css({"border-color": "#d3d3d3", "box-shadow": "none"});
            $(this).siblings(":last").css("display", "none");
            $(this).next().css("display", "block");
            err = 0;
        } else {
            err = 1;
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
            $(this).next().css("display", "none");
            $(this).siblings(":last").css("display", "block");
        }
    });

    $("#signup_form input[name='retype_password']").on("keyup change blur", function () {
        let input_value = $(this).val();
        if (input_value == "") {
            $("#signup_re_pass_err").text("Retype Password is Empty").css("display", "block");
        } else {
            $("#signup_re_pass_err").css("display", "none");

        }
        let pass_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;//Example = Bd12345678

        if (pass_regex.test(input_value)) {
            $(this).css({"border-color": "#d3d3d3", "box-shadow": "none"});
            $(this).siblings(":last").css("display", "none");
            $(this).next().css("display", "block");
            err = 0;
        } else {
            err = 1;
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
            $(this).next().css("display", "none");
            $(this).siblings(":last").css("display", "block");
        }
    });

    $("#signup_form input[type='submit']").on("click", function (event) {
        event.preventDefault();

        let input_list = $("#signup_form .input_group input");
        for (var i = 0; i < input_list.length; i++) {
            if (input_list[i].value === "") {
                input_list[i].style.borderColor = "red";
                input_list[i].style.boxShadow = "-1px 0px 1px 2px red";
                $("#fulname_err").text("Please Fullname recheck").css("display", "block");
                $("#email_err").text("Please Email recheck.").css("display", "block");
                $("#signup_pass_err").text("Please Password recheck").css("display", "block");
                $("#signup_re_pass_err").text("Please Retype Password recheck").css("display", "block");
                err = 1;
            } else {
//                            console.log(input_list[i].value);
//                             err = 0;
            }
        }

        if (err === 0) {
            $("#signup_form").submit();
        } else {
            $(this).css({"border-color": "red", "box-shadow": "-1px 0px 1px 2px red"});
        }
    });


//    for order view page tab link
    $(".view_tab ul li").on("click", function (event) {
        
        $(".view_tab ul").children().removeClass("tab_active");
        $(this).addClass("tab_active");
        
        $(".view_panel").children().removeClass("show");
        $(".view_panel").children().addClass("d-none");
        
        tab_panel = this.attributes["tab-id"].value;
        $("#"+tab_panel).removeClass("d-none");
        $("#"+tab_panel).addClass("show");
        
    });
    
    
//    for payment list
     $(".payment-list li").on("click", function (event) {
         $(".payment-list").children().removeClass("payment_active");
         $(this).addClass("payment_active");
     });
     
//     for delivery type
     $(".delivery_type li").on("click", function (event) {
         
         $(".delivery_type").children().removeClass("d_active");
         $(this).addClass("d_active");
         
        $(".delivery_addr_panel").children().removeClass("show");
        $(".delivery_addr_panel").children().addClass("d-none");
         
        tab_panel = this.attributes["tab-id"].value;
        $("#"+tab_panel).removeClass("d-none");
        $("#"+tab_panel).addClass("show");
     });


   //add to shopping cart
     $(".add_cart_item").on("click", function(event) {
        product_id = this.attributes["product-id"].value;
        $.get("/public/add_cart/"+product_id, function (data, status) {
            if (status === "success") {
//               console.log("successful")
                 $.get("/public/cart_item", function (data2, status2) {
//                      console.log(data2)
                      if (status === "success") {
                         $("#cart_item").html(data2)
                      }
                 });
            }
        });
     });


});




function userMenu(ele) {
    let menu = document.getElementById('user_profile_menu');
    menu.classList.toggle("show");

    document.addEventListener("click", function (event) {
        if (event.target !== ele) {
            menu.className = menu.className.replace("show", "");
        }
    });
//    console.log("Hello")
}