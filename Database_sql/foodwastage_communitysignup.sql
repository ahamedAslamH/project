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
-- Table structure for table `communitysignup`
--

DROP TABLE IF EXISTS `communitysignup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communitysignup` (
  `cuid` varchar(45) NOT NULL,
  `cuphoto` varchar(30) DEFAULT NULL,
  `orgname` varchar(45) DEFAULT NULL,
  `comname` varchar(45) DEFAULT NULL,
  `ctype` varchar(45) DEFAULT NULL,
  `cemail` varchar(45) DEFAULT NULL,
  `cphno` varchar(10) DEFAULT NULL,
  `caddress` varchar(200) DEFAULT NULL,
  `regcertphoto` varchar(45) DEFAULT NULL,
  `regcertnumber` varchar(45) DEFAULT NULL,
  `cpassword` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communitysignup`
--

LOCK TABLES `communitysignup` WRITE;
/*!40000 ALTER TABLE `communitysignup` DISABLE KEYS */;
INSERT INTO `communitysignup` VALUES ('CUI-0626b3','anbu.jpg','Anbu Sankar M','Anbu Marriage Hall','8778516691','anbusankar2522@gmail.com','8778516691','Lawspet','communityregisterationphoto.jpg','ETYAUAB03287467','1234'),('CUI-36ae04','Johnwick.jpg','sheva','sheva foods','254784216','sheva@gmail.com','254784216','chennai','johnwick1.jpg','1234','12345678'),('CUI-cfe8d7','john.jpg','SIVASANKARAN','INDIAN','99898989','SANKARSVISION@GMAIL.COM','99898989','Puducherry, Tamil Nadu.','idly.jpg','ETYAUAB03287467','SIVA');
/*!40000 ALTER TABLE `communitysignup` ENABLE KEYS */;
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
