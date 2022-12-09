-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: webnike_erp
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(45) NOT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Administration'),(2,'Human Resource'),(3,'Sales'),(4,'Production');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_detail`
--

DROP TABLE IF EXISTS `employee_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_detail` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(45) DEFAULT NULL,
  `employee_address` varchar(45) DEFAULT NULL,
  `employee_city` varchar(45) DEFAULT NULL,
  `employee_contact_no` varchar(45) DEFAULT NULL,
  `employee_manager_id` int DEFAULT NULL,
  `employee_department_id` int DEFAULT NULL,
  `designation` varchar(45) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `cnic` varchar(45) DEFAULT NULL,
  `bank_account_title` varchar(60) DEFAULT NULL,
  `personal_email` varchar(60) DEFAULT NULL,
  `bank_account_number` varchar(150) DEFAULT NULL,
  `register_date` date DEFAULT NULL,
  `employee_role_id` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `department_id_idx` (`employee_department_id`),
  KEY `manager_id_idx` (`employee_manager_id`),
  KEY `role_id_idx` (`employee_role_id`),
  CONSTRAINT `department_id` FOREIGN KEY (`employee_department_id`) REFERENCES `department` (`department_id`),
  CONSTRAINT `manager_id` FOREIGN KEY (`employee_manager_id`) REFERENCES `employee_detail` (`employee_id`),
  CONSTRAINT `role_id` FOREIGN KEY (`employee_role_id`) REFERENCES `user_role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_detail`
--

LOCK TABLES `employee_detail` WRITE;
/*!40000 ALTER TABLE `employee_detail` DISABLE KEYS */;
INSERT INTO `employee_detail` VALUES (1,'Sultan','Webnike, Gulshan','Karachi','0300000000000',NULL,1,'Admin',NULL,'1990-01-01','42101-12345-6','Sultan','sultan@gmail.com','1234567890','2022-10-24',1),(2,'Zarnish','Webnike, Gulshan','Karachi','0300000000000',1,2,'Hr Manager',15000,'1990-01-01','42101-12345-1','Zarnish','zarnish@gmail.com','1234567890','2022-10-24',2),(3,'Sharjeel','Webnike, Gulshan','Karachi','0300000000000',1,4,'Development Manager',15000,'1990-01-01','42101-12347-3','Sharjeel Faisal','sharjeel@gmail.com','1234567890','2022-10-24',4),(4,'Warisha','Webnike, Gulshan','Karachi','0300000000000',1,4,'Writer Manager',20000,'1990-01-01','42101-12349-2','Warish','warisha@gmail.com','1234567890','2022-10-24',5),(5,'zeeshan','Webnike, Gulshan','Karachi','0300000000000',1,3,'Sales Manager',150000,'1990-01-01','42101-12341-4','Zeeshan','zeeshan@gmail.com','1234567890','2022-10-24',3),(9,'Abbas','C-5, Block-5, Gulshan-e-Iqbal','Karachi','+923000000002',2,4,'Full Stack Developer',45000,'2022-02-02','42101-1234567-1','Mustufa Abbas','abbas@gmail.com','1234567890','2022-10-24',4),(10,'Ali','C-6, Block-5, Gulshan-e-Iqbal','Karachi','+923000000000',2,4,'Python Developer',40000,'2022-10-06','42101-1234567-6','Ali Shah','ali@gmail.com','1234567891','2022-10-24',4),(11,'Qadama','C-7, Block-5, Gulshan-e-Iqbal','Karachi','+923000000000',2,4,'PHP Developer',45000,'2022-10-29','42101-1234567-3','Muhammad Qadama','qadama@gmail.com','1234567892','2022-10-24',4),(13,'Muaaz','C-8, Block-5, Gulshan-e-Iqbal','Karachi','+923000000000',2,4,'Full Stack Developer',20000,'2022-05-12','42101-1234567-4','Muaaz Siddiq','muaaz@gmail.com','12345678904','2022-10-25',4),(15,'Sherish','C-8, Block-5, Gulshan-e-Iqbal','Karachi','+923000000000',1,2,'Hr lead',60000,'2022-10-06','42101-1234569-9','Sherish','sherish@gmail.com','123456789023','2022-10-25',2),(16,'Ashar','C-10, Block-5, Gulshan-e-Iqbal','Karachi','+923000000000',2,4,'Word Press',30000,'2022-10-12','42101-1234568-1','Asher','asher@gmail.com','1234567890123','2022-10-25',4),(24,'M.Umar','A-12, D.H.A, Phase-2 ','Karachi','+923000000001',3,3,'Marketing manager',100000,'2020-02-12','43101-1234567-8','Muhammad Umar','umar@gmail.com','12345678904','2022-10-28',3),(25,'Alina','C-30, Clifton, Karachi','Karachi','+923000000000',3,3,'Bidder',40000,'2022-07-06','42501-1234567-9','Alina','alina@webnike','1234567892','2022-10-28',3),(31,'Ashir','A-1, Bufferzone','Karachi','+923000000000',2,4,'Intern',10000,'2022-10-12','72101-1234568-1','ashir','ashir@gmail.com','1234567890123','2022-10-29',4),(32,'Waseem','A-1, Bufferzone','Karachi','+923000000000',1,4,'Manager E-commerce',70000,'2022-02-09','72101-1234568-6','Waseem','waseem@gmail.com','1234567890123','2022-10-29',4),(33,'Arsalan','B-20, 11-B, North Karachi','Karachi','+923000000000',1,2,'Hiring Manager',60000,'2022-10-10','72101-1234568-3','Arsalan Ali','arsalan@gmail.com','12345678904','2022-10-29',2);
/*!40000 ALTER TABLE `employee_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_credential`
--

DROP TABLE IF EXISTS `login_credential`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_credential` (
  `login_email` varchar(50) NOT NULL,
  `login_password` varchar(45) NOT NULL,
  `employee_id_fk` int NOT NULL,
  `user_role_fk` int NOT NULL,
  `department_id_fk` int DEFAULT NULL,
  `active` varchar(10) NOT NULL,
  PRIMARY KEY (`login_email`),
  KEY `employee_id_idx` (`employee_id_fk`),
  KEY `user_role_fk2_idx` (`user_role_fk`),
  KEY `department_id_fk2_idx` (`department_id_fk`),
  CONSTRAINT `department_id_fk2` FOREIGN KEY (`department_id_fk`) REFERENCES `department` (`department_id`) ON DELETE CASCADE,
  CONSTRAINT `employee_id` FOREIGN KEY (`employee_id_fk`) REFERENCES `employee_detail` (`employee_id`),
  CONSTRAINT `user_role_fk2` FOREIGN KEY (`user_role_fk`) REFERENCES `user_role` (`role_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_credential`
--

LOCK TABLES `login_credential` WRITE;
/*!40000 ALTER TABLE `login_credential` DISABLE KEYS */;
INSERT INTO `login_credential` VALUES ('abbas@webnike','webnike',9,4,4,'1'),('ahsar@webnike','webnike',16,4,4,'1'),('ali@webnike.com','webnike',10,4,4,'1'),('alina@webnike','webnike',25,3,3,'0'),('arsalan@webnike','webnike',33,2,2,'1'),('ashir@webnike','webnike',31,4,4,'1'),('muaaz@webnike','webnike',13,4,4,'1'),('qadama@webnike','webnike',11,4,4,'1'),('sharjeel@webnike','webnike',3,4,4,'1'),('sherish@webnike','webnike',15,2,2,'1'),('sultan@webnike','webnike',1,1,1,'1'),('umar@webnike','webnike',24,3,3,'1'),('warisha@webnike','webnike',4,5,4,'1'),('waseem@webnike','webnike',32,4,4,'1'),('zarnish@webnike','webnike',2,2,2,'1'),('zeeshan@webnike','webnike',5,3,3,'1');
/*!40000 ALTER TABLE `login_credential` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_table`
--

DROP TABLE IF EXISTS `manager_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_table` (
  `manager_id` int NOT NULL AUTO_INCREMENT,
  `manager_name` varchar(75) DEFAULT NULL,
  `manager_department` varchar(300) DEFAULT NULL,
  `manager_emp_id` int DEFAULT NULL,
  PRIMARY KEY (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_table`
--

LOCK TABLES `manager_table` WRITE;
/*!40000 ALTER TABLE `manager_table` DISABLE KEYS */;
INSERT INTO `manager_table` VALUES (1,'Sultan','Administration',1),(2,'Sharjeel','Production - Developer',3),(3,'Zeeshan','Sales',5),(4,'Zarnish','Hr',2),(5,'Warisha','Production - Writer',4),(9,'Waseem','Production - Developer',32),(13,'Arsalan','Human Resource - Hr',33);
/*!40000 ALTER TABLE `manager_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_detail`
--

DROP TABLE IF EXISTS `order_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_detail` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_title` varchar(45) DEFAULT NULL,
  `order_date` datetime DEFAULT NULL,
  `sale_agent_id` int DEFAULT NULL,
  `order_type` enum('pre-order','order') DEFAULT 'pre-order',
  `order_complete` tinyint NOT NULL DEFAULT '0',
  `client_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `sale_agent_id_idx` (`sale_agent_id`),
  CONSTRAINT `sale_agent_id` FOREIGN KEY (`sale_agent_id`) REFERENCES `employee_detail` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_detail`
--

LOCK TABLES `order_detail` WRITE;
/*!40000 ALTER TABLE `order_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_employee_association`
--

DROP TABLE IF EXISTS `order_employee_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_employee_association` (
  `order_association_id` int NOT NULL AUTO_INCREMENT,
  `order_id_fk` int NOT NULL,
  `employee_id_fk` int NOT NULL,
  `datetime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_association_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_employee_association`
--

LOCK TABLES `order_employee_association` WRITE;
/*!40000 ALTER TABLE `order_employee_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_employee_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_price`
--

DROP TABLE IF EXISTS `order_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_price` (
  `price_id` int NOT NULL,
  `order_price` int NOT NULL,
  `revised_id` int DEFAULT NULL,
  `order_id` int NOT NULL,
  PRIMARY KEY (`price_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_price`
--

LOCK TABLES `order_price` WRITE;
/*!40000 ALTER TABLE `order_price` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_entry`
--

DROP TABLE IF EXISTS `payment_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_entry` (
  `payment_id` int NOT NULL,
  `user_id` int NOT NULL,
  `salary` int DEFAULT NULL,
  `commission` int DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_entry`
--

LOCK TABLES `payment_entry` WRITE;
/*!40000 ALTER TABLE `payment_entry` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(45) NOT NULL,
  `department_id_fk` int DEFAULT NULL,
  PRIMARY KEY (`role_id`),
  KEY `department_id_fk3_idx` (`department_id_fk`),
  CONSTRAINT `department_id_fk3` FOREIGN KEY (`department_id_fk`) REFERENCES `department` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES (1,'Admin',1),(2,'Hr',2),(3,'Sales',3),(4,'Developer',4),(5,'Writer',4);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-02 15:47:52
