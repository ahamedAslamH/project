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
-- Table structure for table `signupentry`
--

DROP TABLE IF EXISTS `signupentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signupentry` (
  `uid` varchar(45) NOT NULL,
  `fname` varchar(30) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `uphoto` varchar(45) DEFAULT NULL,
  `phno` varchar(10) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `pname` varchar(45) DEFAULT NULL,
  `pnumber` varchar(45) DEFAULT NULL,
  `pfile` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signupentry`
--

LOCK TABLES `signupentry` WRITE;
/*!40000 ALTER TABLE `signupentry` DISABLE KEYS */;
INSERT INTO `signupentry` VALUES ('UI-04d08b','A','S','tom.jpg','8754905350','as2522@gmail.com','Lawspet','Aadhar Card','2954 5785 1523','communityregisterationphoto.jpg','12345678'),('UI-884a0e','Ahamed Aslam','H','aslam.jpg','9361333314','aslammm0510@gmail.com','Sultanepet','Aadhar Card','8990 3556 2222','aadhar id.jpg','1234'),('UI-efeba6','Immanuvel','A','imman.jpg','8248754186','immanvj077@gmail.com','Reddiarpalayam','Pan Card','DXTPA7438B','pancard id.jpg','1234');
/*!40000 ALTER TABLE `signupentry` ENABLE KEYS */;
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
