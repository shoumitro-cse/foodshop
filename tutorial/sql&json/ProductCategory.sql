-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 24, 2020 at 08:58 AM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `ProductCategory`
--

CREATE TABLE `ProductCategory` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ProductCategory`
--

INSERT INTO `ProductCategory` (`id`, `name`, `category_id`) VALUES
(1700000, 'Baby Food', 3000000),
(1700001, 'Bath & Skin Care', 3000000),
(1700002, 'Diapers & wipes', 3000000),
(1700003, 'Breads', 3000001),
(1700004, 'Cakes', 3000001),
(1700005, 'Cookies', 3000001),
(1700006, 'Antiseptics', 3000002),
(1700007, 'Bath', 3000002),
(1700008, 'Deodorants', 3000002),
(1700009, 'Face & Body Care', 3000002),
(1700010, 'Family Planning', 3000002),
(1700011, 'Feminine Cares', 3000002),
(1700012, 'First Aid', 3000002),
(1700013, 'Hair Care', 3000002),
(1700014, 'Hand Wash & Sanitizer', 3000002),
(1700015, 'Oral Care', 3000002),
(1700016, 'Shaving care', 3000002),
(1700017, 'Skin Care', 3000002),
(1700018, 'Health Drink, Supplement', 3000003),
(1700019, 'Juice', 3000003),
(1700020, 'Soft Drinks', 3000003),
(1700021, 'Tea and Coffee', 3000003),
(1700022, 'Water', 3000003),
(1700023, 'Butter', 3000004),
(1700024, 'Cheese', 3000004),
(1700025, 'Liquid & UHT Milk', 3000004),
(1700026, 'Milk Powder', 3000004),
(1700027, 'Yogurt', 3000004),
(1700028, 'Fresh Fish', 3000005),
(1700029, 'Dry Fish', 3000005),
(1700030, 'Fruits', 3000006),
(1700031, 'Vegetables', 3000006),
(1700032, 'Atta, Flour & Suji', 3000007),
(1700033, 'Canned Food', 3000007),
(1700034, 'Candy & Chocolates', 3000007),
(1700035, 'Cereals', 3000007),
(1700036, 'Chips', 3000007),
(1700037, 'Cooking Oil Ghee', 3000007),
(1700038, 'Dips & Spreads', 3000007),
(1700039, 'Egg', 3000007),
(1700040, 'Frozen food', 3000007),
(1700041, 'Noodles', 3000007),
(1700042, 'Oats', 3000007),
(1700043, 'Pasta', 3000007),
(1700044, 'Popcorns and Nuts', 3000007),
(1700045, 'Puffed Rice', 3000007),
(1700046, 'Pulse', 3000007),
(1700047, 'Rice', 3000007),
(1700048, 'Sauces', 3000007),
(1700049, 'Salt,Sugar & Honey', 3000007),
(1700050, 'Soup', 3000007),
(1700051, 'Spice and Condiments', 3000007),
(1700052, 'Air Fresheners', 3000008),
(1700053, 'Cleaning Supplies', 3000008),
(1700054, 'Detergents & Dishwashes', 3000008),
(1700055, 'Food Stoarge', 3000008),
(1700056, 'Kitchen Accessories', 3000008),
(1700057, 'Pest Control', 3000008),
(1700058, 'Tissue & Napkin', 3000008),
(1700059, 'Beef & Mutton', 3000009),
(1700060, 'Chicken', 3000009),
(1700061, 'Cat Food', 3000010),
(1700062, 'Dog Food', 3000010);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ProductCategory`
--
ALTER TABLE `ProductCategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ProductCategory_category_id_8566a563_fk_Category_id` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ProductCategory`
--
ALTER TABLE `ProductCategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1700063;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ProductCategory`
--
ALTER TABLE `ProductCategory`
  ADD CONSTRAINT `ProductCategory_category_id_8566a563_fk_Category_id` FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
