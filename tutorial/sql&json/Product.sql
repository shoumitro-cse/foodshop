-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 28, 2020 at 10:02 AM
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
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `keyword` varchar(5000) NOT NULL,
  `weight` varchar(255) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `currentStock` int(11) NOT NULL,
  `price` double NOT NULL,
  `unitPrice` double NOT NULL,
  `taxed` double NOT NULL,
  `discount_id` int(11) NOT NULL,
  `productCategory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`id`, `name`, `keyword`, `weight`, `brand`, `stock`, `currentStock`, `price`, `unitPrice`, `taxed`, `discount_id`, `productCategory_id`) VALUES
(6000000, 'Banana (Sagor) [1 Pc.]', 'banana-sagor-1-pc', '1  kg', 'Brand', 13, 13, 20, 20, 0, 5000001, 1700030),
(6000001, 'Deshi Tomato', 'deshi-tomato-12-kg', '12 kg', 'Brand', 16, 16, 440, 440, 0, 5000001, 1700030),
(6000002, 'Kenu Orange Australian', 'kenu-orange-australian', '12 kg', 'Brand', 13, 13, 278, 278, 0, 5000001, 1700030),
(6000003, 'Pomegranate', 'pomegranate-10-kg', '10 kg', 'Brand', 34, 34, 450, 450, 0, 5000001, 1700030),
(6000004, 'Nashpati (White Pear)', 'nashpati-white-pear-1-kg', '1  kg', 'Brand', 45, 45, 250, 250, 0, 5000001, 1700030),
(6000005, 'Nashpati Red [Pear Red]', 'nashpati-red-pear-red-2kg', '2kg', 'Brand', 23, 23, 349, 349, 0, 5000001, 1700030),
(6000006, 'Malta Green', 'malta-green-2kg', '2kg', 'Brand', 23, 23, 550, 550, 0, 5000000, 1700030),
(6000007, 'Lotkon Bulk', 'lotkon-bulk-3-kg', '3 kg', 'Brand', 3, 3, 180, 180, 0, 5000001, 1700030),
(6000008, 'Coconut', 'coconut-1-pc', '1 pc', 'Brand', 45, 45, 70, 70, 0, 5000001, 1700030),
(6000009, 'Paka Pepe Thai.', 'paka-pepe-thai-1-kg', '1 kg', 'Brand', 23, 23, 120, 120, 0, 5000001, 1700030),
(6000010, 'Thai Guava', 'thai-guava-10-pc', '10 pc', 'Brand', 23, 23, 75, 75, 0, 5000001, 1700030),
(6000011, 'Orange 1kg', 'orange-1kg-1-kg', '1 kg', 'No Brand', 34, 34, 320, 320, 0, 5000001, 1700030);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Product`
--
ALTER TABLE `Product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Product_productCategory_id_0de3b6b9_fk_ProductCategory_id` (`productCategory_id`),
  ADD KEY `Product_discount_id_16b0f032_fk_Discount_id` (`discount_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Product`
--
ALTER TABLE `Product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6000012;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Product`
--
ALTER TABLE `Product`
  ADD CONSTRAINT `Product_discount_id_16b0f032_fk_Discount_id` FOREIGN KEY (`discount_id`) REFERENCES `Discount` (`id`),
  ADD CONSTRAINT `Product_productCategory_id_0de3b6b9_fk_ProductCategory_id` FOREIGN KEY (`productCategory_id`) REFERENCES `ProductCategory` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
