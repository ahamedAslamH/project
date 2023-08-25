-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: foodwastage
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `communityentry`
--

DROP TABLE IF EXISTS `communityentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communityentry` (
  `cfid` varchar(45) NOT NULL,
  `cuid` varchar(30) DEFAULT NULL,
  `cuname` varchar(45) DEFAULT NULL,
  `cemail` varchar(45) DEFAULT NULL,
  `cphno` varchar(45) DEFAULT NULL,
  `cfdname` varchar(45) DEFAULT NULL,
  `cfdtype` varchar(45) DEFAULT NULL,
  `cfdq` varchar(45) DEFAULT NULL,
  `caddress` varchar(45) DEFAULT NULL,
  `cphoto` varchar(45) DEFAULT NULL,
  `cfrdate` varchar(45) DEFAULT NULL,
  `cexdate` varchar(45) DEFAULT NULL,
  `cfrtime` varchar(45) DEFAULT NULL,
  `cextime` varchar(45) DEFAULT NULL,
  `corderconform` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cfid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communityentry`
--

LOCK TABLES `communityentry` WRITE;
/*!40000 ALTER TABLE `communityentry` DISABLE KEYS */;
INSERT INTO `communityentry` VALUES ('CFI-526ebd','CUI-0626b3','Anbu Sankar M','anbusankar2522@gmail.com','8778516691','Sambar','Veg','30-40 members','Ottur Street, Chennai','sambar.jpg','2023-07-01','2023-07-02','10:44 AM','09:44 AM','pending'),('CFI-5a45a1','CUI-36ae04','sheva','sheva@gmail.com','254784216','poori','Veg','8-12 member','Kathirkamam','poori.jpg','2023-06-22','2023-06-23','06:21 PM','02:21 AM','pending'),('CFI-70db9e','CUI-36ae04','sheva','sheva@gmail.com','254784216','poori','Veg','12-16 member','chennai','poori.jpg','2023-06-20','2023-06-21','11:14 AM','06:14 PM','pending'),('CFI-f2d04e','CUI-36ae04','sheva','sheva@gmail.com','254784216','Sambar','Veg','16-20 member','Reddiarpalayam','sambar.jpg','2023-06-20','2023-06-21','11:18 AM','11:18 AM','pending');
/*!40000 ALTER TABLE `communityentry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-25 22:10:18
