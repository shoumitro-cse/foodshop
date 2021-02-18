-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 28, 2020 at 10:03 AM
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
-- Table structure for table `ProductInfo`
--

CREATE TABLE `ProductInfo` (
  `id` int(11) NOT NULL,
  `desc1` varchar(255) NOT NULL,
  `desc2` varchar(255) NOT NULL,
  `desc3` varchar(255) NOT NULL,
  `desc4` varchar(255) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `image3` varchar(100) NOT NULL,
  `image4` varchar(100) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ProductInfo`
--

INSERT INTO `ProductInfo` (`id`, `desc1`, `desc2`, `desc3`, `desc4`, `image1`, `image2`, `image3`, `image4`, `product_id`) VALUES
(7000000, 'Loaded with fiber, both soluble and insoluble.', 'Banana is a heavyweight when it comes to nutrition.', 'It also contains fiber, potassium, folate, and antioxidants.', 'It can also be a good way to get magnesium and vitamins C and B6.', 'product/banana.jpg', 'product/banana_hliKdf1.jpg', 'product/banana_RQLWklI.jpg', 'product/banana_HILJ8iF.jpg', 6000000),
(7000001, 'Tomatoes are the major dietary source of the antioxidant lycopene, which has been linked to many health benefits, including reduced risk of heart disease and cancer.', 'They are also a great source of vitamin C, potassium, folate, and vitamin K.', 'The water content of tomatoes is around 95%. The other 5% consists mainly of carbohydrates and fiber.', 'Fresh tomatoes are low in carbs.', 'product/tomato.jpg', 'product/tomato_ijK1Vsz.jpg', 'product/tomato_3qM4bKr.jpg', 'product/tomato_smgyw5O.jpg', 6000001),
(7000002, 'The \'Kinnow\' is a high yield mandarin hybrid cultivated extensively in the wider Punjab region of India and Pakistan.', 'It is a hybrid of two citrus cultivars \'King\' (Citrus nobilis) × \'Willow Leaf\' (Citrus × deliciosa) first developed by Howard B. Frost, at the University of California Citrus Experiment Station.', 'ab', 'abc', 'product/orange.jpg', 'product/orange_sLUMv2B.jpg', 'product/orange_fj755op.jpg', 'product/orange_xibz6gk.jpg', 6000002),
(7000003, 'Protects us from free radicals.', 'It thins your blood. Prevention of atherosclerosis.', 'It acts as an oxygen mask.', 'It acts as an oxygen mask.', 'product/Pomegranate.jpg', 'product/Pomegranate_Efhbcjp.jpg', 'product/Pomegranate_H8cC6sz.jpg', 'product/Pomegranate_4hSRsoI.jpg', 6000003),
(7000004, 'Helps in Weight Loss.', 'Pear, because of its low caloric value, is good to include in your diet aimed at shedding weight.', 'Prevents Cancer. Combats Cardiovascular Diseases. Reduced Risk of Colitis.', 'Prevents Cancer. Combats Cardiovascular Diseases. Reduced Risk of Colitis.', 'product/Nashpati.jpg', 'product/Nashpati_FSp9eHi.jpg', 'product/Nashpati_KkbSPSC.jpg', 'product/Nashpati_L7bk6Fh.jpg', 6000004),
(7000005, 'Helps in Weight Loss.', 'Pear, because of its low caloric value, is good to include in your diet aimed at shedding weight.', 'Prevents Cancer. Combats Cardiovascular Diseases. Reduced Risk of Colitis.', 'Prevents Cancer. Combats Cardiovascular Diseases. Reduced Risk of Colitis.', 'product/Nashpati_RED.jpg', 'product/Nashpati_RED_nESHIqR.jpg', 'product/Nashpati_RED_LaQCDrK.jpg', 'product/Nashpati_RED_a2IsN0l.jpg', 6000005),
(7000006, 'The fruit is rich in vitamins, minerals, and antioxidants.', 'Nutrients include potassium, vitamin C, folate, manganese, dietary fiber, and magnesium.', 'Prevents skin damage. Keeps blood pressure under check.', 'Prevents skin damage. Keeps blood pressure under check.', 'product/MaltaGreen.jpg', 'product/MaltaGreen_6pqYd4r.jpg', 'product/MaltaGreen_UONg6fi.jpg', 'product/MaltaGreen_7sFqUoP.jpg', 6000006),
(7000007, 'Lotkon is a species of', 'fruit tree which grows wild in parts of Southeast Asia and is cultivated for its fruit in Bangladesh, Thailand and Peninsular Malaysia.', 'Its common names include rambai and rambi, and in Thai language mafai-farang.', 'It is claimed that lotkon have more nutritional value than many other popular fruits.', 'product/LotkonBulk.jpg', 'product/LotkonBulk_ZMGCjT1.jpg', 'product/LotkonBulk_UPpAu61.jpg', 'product/LotkonBulk_KUoQhkv.jpg', 6000007),
(7000008, 'Coconut is the fruit of the coconut palm', '- It\'s used for its water, milk, oil, and tasty meat', 'Coconuts have been grown in tropical regions for more than 4,500 years 4-but', 'recently increased in popularity for their flavor, culinary uses, and potential health benefits', 'product/Coconut.jpg', 'product/Coconut_yckcw7q.jpg', 'product/Coconut_bBJugwM.jpg', 'product/Coconut_eIZiid0.jpg', 6000008),
(7000009, 'Papaya is rich in fiber, Vitamin C, and antioxidants which prevent cholesterol build up in your arteries.', 'Those looking to lose weight must include papaya in their diet as it is very low in calories.', 'A single papaya contains more than 200% of your daily requirement of Vitamin C, making it great for your immunity.', 'Helps ease menstrual pain.', 'product/Pepe.jpg', 'product/Pepe_wckJr7V.jpg', 'product/Pepe_vy8KmdE.jpg', 'product/Pepe_VeWKwSi.jpg', 6000009),
(7000010, 'Thai guavas contain vitamin B3 and B6, which improves blood circulation to the brain.', 'It prevents the growth of cancer cells.', 'It improves the sodium and potassium balance of the body, resulting in regulated blood pressure.', 'One of the richest sources of fiber, compared to other fruits.', 'product/Guava_.jpg', 'product/Guava__KVBfxNC.jpg', 'product/Guava__mAGuJvR.jpg', 'product/Guava__MpY80AP.jpg', 6000010),
(7000011, 'Oranges are an excellent source of vitamin C.', 'Antioxidants in oranges help protect skin from free radical damage known to cause signs of aging.', 'Oranges, being rich in Vitamins B6, help support the production of hemoglobin', 'Controls blood sugar levels.', 'product/Orange.jpg', 'product/Orange_MvknyiQ.jpg', 'product/Orange_DGGc36i.jpg', 'product/Orange_HNOisE8.jpg', 6000011);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ProductInfo`
--
ALTER TABLE `ProductInfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `product_id` (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ProductInfo`
--
ALTER TABLE `ProductInfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7000012;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ProductInfo`
--
ALTER TABLE `ProductInfo`
  ADD CONSTRAINT `ProductInfo_product_id_f5e6d815_fk_Product_id` FOREIGN KEY (`product_id`) REFERENCES `Product` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
