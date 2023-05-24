/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - temple
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`temple` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `temple`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add auditorium',7,'add_auditorium'),
(26,'Can change auditorium',7,'change_auditorium'),
(27,'Can delete auditorium',7,'delete_auditorium'),
(28,'Can view auditorium',7,'view_auditorium'),
(29,'Can add chitti',8,'add_chitti'),
(30,'Can change chitti',8,'change_chitti'),
(31,'Can delete chitti',8,'delete_chitti'),
(32,'Can view chitti',8,'view_chitti'),
(33,'Can add chitti_details',9,'add_chitti_details'),
(34,'Can change chitti_details',9,'change_chitti_details'),
(35,'Can delete chitti_details',9,'delete_chitti_details'),
(36,'Can view chitti_details',9,'view_chitti_details'),
(37,'Can add committee',10,'add_committee'),
(38,'Can change committee',10,'change_committee'),
(39,'Can delete committee',10,'delete_committee'),
(40,'Can view committee',10,'view_committee'),
(41,'Can add login',11,'add_login'),
(42,'Can change login',11,'change_login'),
(43,'Can delete login',11,'delete_login'),
(44,'Can view login',11,'view_login'),
(45,'Can add members',12,'add_members'),
(46,'Can change members',12,'change_members'),
(47,'Can delete members',12,'delete_members'),
(48,'Can view members',12,'view_members'),
(49,'Can add program',13,'add_program'),
(50,'Can change program',13,'change_program'),
(51,'Can delete program',13,'delete_program'),
(52,'Can view program',13,'view_program'),
(53,'Can add videos',14,'add_videos'),
(54,'Can change videos',14,'change_videos'),
(55,'Can delete videos',14,'delete_videos'),
(56,'Can view videos',14,'view_videos'),
(61,'Can add user',16,'add_user'),
(62,'Can change user',16,'change_user'),
(63,'Can delete user',16,'delete_user'),
(64,'Can view user',16,'view_user'),
(65,'Can add committe_program',17,'add_committe_program'),
(66,'Can change committe_program',17,'change_committe_program'),
(67,'Can delete committe_program',17,'delete_committe_program'),
(68,'Can view committe_program',17,'view_committe_program'),
(69,'Can add chitti_payment',18,'add_chitti_payment'),
(70,'Can change chitti_payment',18,'change_chitti_payment'),
(71,'Can delete chitti_payment',18,'delete_chitti_payment'),
(72,'Can view chitti_payment',18,'view_chitti_payment'),
(73,'Can add bank',19,'add_bank'),
(74,'Can change bank',19,'change_bank'),
(75,'Can delete bank',19,'delete_bank'),
(76,'Can view bank',19,'view_bank'),
(77,'Can add auditorium_payment',20,'add_auditorium_payment'),
(78,'Can change auditorium_payment',20,'change_auditorium_payment'),
(79,'Can delete auditorium_payment',20,'delete_auditorium_payment'),
(80,'Can view auditorium_payment',20,'view_auditorium_payment'),
(81,'Can add auditorium_booking',21,'add_auditorium_booking'),
(82,'Can change auditorium_booking',21,'change_auditorium_booking'),
(83,'Can delete auditorium_booking',21,'delete_auditorium_booking'),
(84,'Can view auditorium_booking',21,'view_auditorium_booking'),
(93,'Can add winner',24,'add_winner'),
(94,'Can change winner',24,'change_winner'),
(95,'Can delete winner',24,'delete_winner'),
(96,'Can view winner',24,'view_winner');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$320000$ft0IPMzh7yRSM9PyaAq7Lf$27Stvjf9Fn1ehtqKHeu7Q6D9LFu6Od+O/7EXHzK259Y=','2022-07-25 04:23:06.551872',1,'admin','','','admin@gmail.com',1,1,'2022-07-25 03:09:44.508215');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'templeapp','auditorium'),
(21,'templeapp','auditorium_booking'),
(20,'templeapp','auditorium_payment'),
(19,'templeapp','bank'),
(8,'templeapp','chitti'),
(9,'templeapp','chitti_details'),
(18,'templeapp','chitti_payment'),
(17,'templeapp','committe_program'),
(10,'templeapp','committee'),
(11,'templeapp','login'),
(12,'templeapp','members'),
(13,'templeapp','program'),
(16,'templeapp','user'),
(14,'templeapp','videos'),
(24,'templeapp','winner');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2022-06-21 06:16:44.931600'),
(2,'auth','0001_initial','2022-06-21 06:16:46.080407'),
(3,'admin','0001_initial','2022-06-21 06:16:46.422889'),
(4,'admin','0002_logentry_remove_auto_add','2022-06-21 06:16:46.453623'),
(5,'admin','0003_logentry_add_action_flag_choices','2022-06-21 06:16:46.480815'),
(6,'contenttypes','0002_remove_content_type_name','2022-06-21 06:16:46.707603'),
(7,'auth','0002_alter_permission_name_max_length','2022-06-21 06:16:46.886113'),
(8,'auth','0003_alter_user_email_max_length','2022-06-21 06:16:46.962124'),
(9,'auth','0004_alter_user_username_opts','2022-06-21 06:16:46.988246'),
(10,'auth','0005_alter_user_last_login_null','2022-06-21 06:16:47.106078'),
(11,'auth','0006_require_contenttypes_0002','2022-06-21 06:16:47.119544'),
(12,'auth','0007_alter_validators_add_error_messages','2022-06-21 06:16:47.132079'),
(13,'auth','0008_alter_user_username_max_length','2022-06-21 06:16:47.271106'),
(14,'auth','0009_alter_user_last_name_max_length','2022-06-21 06:16:47.399786'),
(15,'auth','0010_alter_group_name_max_length','2022-06-21 06:16:47.451682'),
(16,'auth','0011_update_proxy_permissions','2022-06-21 06:16:47.480663'),
(17,'auth','0012_alter_user_first_name_max_length','2022-06-21 06:16:47.622772'),
(18,'sessions','0001_initial','2022-06-21 06:16:47.708783'),
(19,'templeapp','0001_initial','2022-06-21 06:16:50.410478'),
(20,'templeapp','0002_committee_email','2022-06-24 14:19:49.904266'),
(21,'templeapp','0003_remove_auditorium_generator','2022-06-27 09:33:55.539684'),
(22,'templeapp','0004_auditorium_booking','2022-06-27 09:37:39.963309'),
(23,'templeapp','0005_auto_20220704_1408','2022-07-04 08:39:34.457674'),
(24,'templeapp','0006_chitti_duration','2022-07-04 08:58:41.589441'),
(25,'templeapp','0007_auto_20220705_1130','2022-07-05 06:01:13.855581'),
(30,'templeapp','0008_winner','2022-07-06 04:44:45.207332'),
(31,'templeapp','0009_alter_bank_ifsc','2022-07-06 06:16:07.063254'),
(32,'templeapp','0010_remove_committe_program_committee_id','2022-07-08 10:50:27.503436'),
(33,'templeapp','0011_remove_auditorium_booking_time','2022-07-13 11:22:17.008572'),
(34,'templeapp','0012_auto_20220713_2302','2022-07-13 17:32:13.850138'),
(35,'templeapp','0013_chitti_date','2022-07-14 06:10:53.806106'),
(36,'templeapp','0014_chitti_status','2022-07-14 07:01:26.530948'),
(37,'templeapp','0015_remove_bank_user_id','2022-07-22 18:00:42.779773'),
(38,'templeapp','0016_remove_chitti_payment_amount_and_more','2022-07-24 06:11:38.324700');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('k4w2mb9pnkguq9vkmrhckgzcr8at2hre','.eJyrVkrOTFGyUjJR0lFKBLGMdJRKCnLBdBmUn5qYrGRloqOUA-Kb6iglZ4B0GAF1pCYXKFkZ6ijl5ueVZADFzJVqAWTvFUE:1oBtEe:clO7hcRYcfkLmddQQTVM2d5ddqDAsPhHEgMmP_yfyBw','2022-07-28 07:26:08.844481');

/*Table structure for table `templeapp_auditorium` */

DROP TABLE IF EXISTS `templeapp_auditorium`;

CREATE TABLE `templeapp_auditorium` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `auditorium_name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `seats` bigint NOT NULL,
  `charge` bigint NOT NULL,
  `advance_charge` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_auditorium` */

insert  into `templeapp_auditorium`(`id`,`auditorium_name`,`place`,`details`,`phone`,`seats`,`charge`,`advance_charge`,`photo`) values 
(2,'AMBIKA ','PALAKUNNU ','KITCHEN,FOOD SEATING ARE AVALABLE ',7845961237,500,250000,4000,'AUDITORIUM_scRstu0.png');

/*Table structure for table `templeapp_auditorium_booking` */

DROP TABLE IF EXISTS `templeapp_auditorium_booking`;

CREATE TABLE `templeapp_auditorium_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `generator` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_auditorium_user_id_id_4db3bbe9_fk_templeapp` (`user_id_id`),
  CONSTRAINT `templeapp_auditorium_user_id_id_4db3bbe9_fk_templeapp` FOREIGN KEY (`user_id_id`) REFERENCES `templeapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_auditorium_booking` */

insert  into `templeapp_auditorium_booking`(`id`,`type`,`details`,`date`,`generator`,`status`,`user_id_id`) values 
(3,'ENGAGEMENT','NIL','2022-07-18','no','approved',7),
(4,'BIRTHDAY FUNCTIONS','Nil','2022-07-21','no','paid',6),
(5,'ENGAGEMENT','Nil','2022-07-28','no','rejected',10),
(6,'BIRTHDAY FUNCTIONS','NIL','2022-08-03','no','paid',8),
(7,'MARRIAGE','nil','2022-08-05','no','approved',6);

/*Table structure for table `templeapp_auditorium_payment` */

DROP TABLE IF EXISTS `templeapp_auditorium_payment`;

CREATE TABLE `templeapp_auditorium_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `current_date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `booking_date` date NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_auditorium_user_id_id_9466cd0b_fk_templeapp` (`user_id_id`),
  CONSTRAINT `templeapp_auditorium_user_id_id_9466cd0b_fk_templeapp` FOREIGN KEY (`user_id_id`) REFERENCES `templeapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_auditorium_payment` */

/*Table structure for table `templeapp_bank` */

DROP TABLE IF EXISTS `templeapp_bank`;

CREATE TABLE `templeapp_bank` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(100) NOT NULL,
  `ifsc` varchar(100) NOT NULL,
  `pin` bigint NOT NULL,
  `acc_no` bigint NOT NULL,
  `amount` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_bank` */

insert  into `templeapp_bank`(`id`,`bank_name`,`ifsc`,`pin`,`acc_no`,`amount`) values 
(1,'SBI','SBI0001',6666,6666,190500);

/*Table structure for table `templeapp_chitti` */

DROP TABLE IF EXISTS `templeapp_chitti`;

CREATE TABLE `templeapp_chitti` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `chitti_amount` bigint NOT NULL,
  `no_members` bigint NOT NULL,
  `winning_amounts` bigint NOT NULL,
  `duration` int NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_chitti` */

insert  into `templeapp_chitti`(`id`,`type`,`details`,`chitti_amount`,`no_members`,`winning_amounts`,`duration`,`date`,`status`) values 
(1,'500 chitti','There would be 3 winners per month',500,78,13000,27,'2022-07-14','pending'),
(4,'200 chitti','There would be 8 winners per month',200,216,5400,28,'2022-07-14','pending');

/*Table structure for table `templeapp_chitti_details` */

DROP TABLE IF EXISTS `templeapp_chitti_details`;

CREATE TABLE `templeapp_chitti_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `chitti_id_id` bigint NOT NULL,
  `member_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_chitti_det_member_id_id_74a4d799_fk_templeapp` (`member_id_id`),
  KEY `templeapp_chitti_det_chitti_id_id_6852c437_fk_templeapp` (`chitti_id_id`),
  CONSTRAINT `templeapp_chitti_det_chitti_id_id_6852c437_fk_templeapp` FOREIGN KEY (`chitti_id_id`) REFERENCES `templeapp_chitti` (`id`),
  CONSTRAINT `templeapp_chitti_det_member_id_id_74a4d799_fk_templeapp` FOREIGN KEY (`member_id_id`) REFERENCES `templeapp_members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_chitti_details` */

insert  into `templeapp_chitti_details`(`id`,`status`,`date`,`chitti_id_id`,`member_id_id`) values 
(17,'pending','2022-07-23',4,3),
(19,'pending','2022-07-23',4,4),
(20,'pending','2022-07-23',4,5),
(21,'pending','2022-07-23',1,2),
(22,'pending','2022-07-23',4,2);

/*Table structure for table `templeapp_chitti_payment` */

DROP TABLE IF EXISTS `templeapp_chitti_payment`;

CREATE TABLE `templeapp_chitti_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `details_id_id` bigint NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_chitti_pay_details_id_id_4d3ca00c_fk_templeapp` (`details_id_id`),
  CONSTRAINT `templeapp_chitti_pay_details_id_id_4d3ca00c_fk_templeapp` FOREIGN KEY (`details_id_id`) REFERENCES `templeapp_chitti_details` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_chitti_payment` */

insert  into `templeapp_chitti_payment`(`id`,`status`,`details_id_id`,`date`) values 
(1,'paid',21,'2022-06-23'),
(2,'paid',21,'2022-07-24'),
(3,'paid',22,'2022-06-15');

/*Table structure for table `templeapp_committe_program` */

DROP TABLE IF EXISTS `templeapp_committe_program`;

CREATE TABLE `templeapp_committe_program` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `program` varchar(100) NOT NULL,
  `venue` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_committe_program` */

insert  into `templeapp_committe_program`(`id`,`program`,`venue`,`date`,`time`) values 
(1,'GENERAL MEETING ','OFFICE HALL  ','2022-07-31','11:30:00.000000');

/*Table structure for table `templeapp_committee` */

DROP TABLE IF EXISTS `templeapp_committee`;

CREATE TABLE `templeapp_committee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `committee_name` varchar(100) NOT NULL,
  `president` varchar(100) NOT NULL,
  `secretary` varchar(100) NOT NULL,
  `no_members` int NOT NULL,
  `phone` bigint NOT NULL,
  `login_id_id` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_committee_login_id_id_a2491ff0_fk_templeapp_login_id` (`login_id_id`),
  CONSTRAINT `templeapp_committee_login_id_id_a2491ff0_fk_templeapp_login_id` FOREIGN KEY (`login_id_id`) REFERENCES `templeapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_committee` */

insert  into `templeapp_committee`(`id`,`committee_name`,`president`,`secretary`,`no_members`,`phone`,`login_id_id`,`email`) values 
(4,'CHIRAMAL PRADESHIKA SAMITHI','NARAYANAN D','CHANDRIKA V',368,9865327410,5,'chiramal321@gmail.com'),
(6,'ARAVATH','NIirmala K K ','Rama T K',600,8907653421,18,'mathrusamithi01@gmail.com'),
(7,'KOPPAL PRADESHIKA SAMITHI','PRABHAKARAN P','BALAKRISHNAN',352,7845961235,37,'koppalpradeshikasamithi@gmail.com');

/*Table structure for table `templeapp_login` */

DROP TABLE IF EXISTS `templeapp_login`;

CREATE TABLE `templeapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `password` varchar(90) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_login` */

insert  into `templeapp_login`(`id`,`user_name`,`password`,`type`) values 
(1,'admin','admin','admin'),
(5,'chiramal','chiramal','committee'),
(16,'rishi','rishi','user'),
(17,'ravi','ravi','REJECTED'),
(18,'mathrusamithi01','mathrusamithi01','committee'),
(19,'ambika','ambika','member'),
(20,'vidya','vidya','member'),
(21,'sheeja','sheeja','member'),
(22,'krishnan','kris123','user'),
(23,'radhika','radhika','member'),
(24,'seetha','seetha','member'),
(25,'meenakshi','meenu','member'),
(26,'anamika','Anamika@23','member'),
(27,'Neethu','NeethuC@23','member'),
(28,'lakshmi','lakshmi','member'),
(29,'parvathi','paru','member'),
(30,'rema','rema','member'),
(31,'raman','raman','member'),
(32,'adi','adi','member'),
(33,'goutham','goutham','member'),
(34,'ravi','ravi','user'),
(35,'varun','varun','pending'),
(36,'sooraj','sooraj','user'),
(37,'koppal','koppal','committee');

/*Table structure for table `templeapp_members` */

DROP TABLE IF EXISTS `templeapp_members`;

CREATE TABLE `templeapp_members` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `house_name` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `pin` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `aadhar_number` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `committee_id_id` bigint NOT NULL,
  `login_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_members_committee_id_id_1d19c130_fk_templeapp` (`committee_id_id`),
  KEY `templeapp_members_login_id_id_8b1de6d5_fk_templeapp_login_id` (`login_id_id`),
  CONSTRAINT `templeapp_members_committee_id_id_1d19c130_fk_templeapp` FOREIGN KEY (`committee_id_id`) REFERENCES `templeapp_committee` (`id`),
  CONSTRAINT `templeapp_members_login_id_id_8b1de6d5_fk_templeapp_login_id` FOREIGN KEY (`login_id_id`) REFERENCES `templeapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_members` */

insert  into `templeapp_members`(`id`,`first_name`,`last_name`,`house_name`,`street`,`post`,`city`,`pin`,`phone`,`aadhar_number`,`email`,`photo`,`committee_id_id`,`login_id_id`) values 
(2,'AMBIKA','R','S M NIVAS','PALAKUNNU','','KASARAGOD',671318,9568741230,874596123025,'ambika@gmail.com','Screenshot (14)_yqbVigg.png',6,19),
(3,'VIDHYA ','S  ','VIDHYA NILAYAM','PALAKUNNU','','KASARAGOD',671318,9889007654,876549003212,'vidyas23@gmail.com','Screenshot 2022-07-05 194434_ukriXi1.png',4,20),
(4,'SHEEJA','K T','S M NIVAS','PALAKUNNU','','KASARAGOD',671318,7994948021,786590403020,'sheejakt64@gmail.com','2022-06-16.png',4,21),
(5,'RADHIKA','C','RADHA NILAYAM','PALAKUNNU','','KASARAGOD',671318,8974561230,897456123566,'radhika23@gmail.com','2022-06-14 (1)_dnHfTvW.png',4,23),
(6,'SEETHA','T','SAISHIVAM','MALAMKUNNU','','KASARAGOD',671318,9865741236,887945612369,'seetha@gmail.com','2022-06-14.png',4,24),
(7,'MEENAKSHI','D','SREE NILAYAM','PALAKUNNU','','KASARAGOD',671319,9865743213,898586848785,'meenu@gmail.com','2022-07-04.png',4,25),
(8,'ANAMIKA','G','ANUPRIYAM','ANGAKALARI','','KASARAGOD',671319,9878757476,8985848786818,'anu123@gmail.com','2022-06-14 (2)_TB7V87M.png',4,26),
(9,'NEETHU','C','KOVVIL VALAPPU','PALAKUNNU','','KASARAGOD',671318,9856323265,898587964123,'neethuc678@gmail.com','2022-06-14 (2)_uMsvQ9M.png',4,27),
(10,'LAKSHMI','H','KUNNUMMAL','MALAMKUNNU','','PALAKUNNU',671318,8527419630,852852874196,'lakshmi@gmail.com','2022-07-03 (1).png',4,28),
(11,'PARVATHI','S','PARVATHI NILAYAM','PALAKUNNU','','KASARAGOD',671318,6598632687,858280838081,'parvathiparu@gmail.com','2022-06-14_VwQWuTN.png',4,29),
(12,'REMA','P','ALAMI VALAPPU','PALAKUNNU','','KASARAGOD',671318,9896959232,858684828081,'remap@gmail.com','2022-06-14_Na5GQBM.png',4,30),
(13,'RAMENDRAN','P P','MELEVALAPPU','PALAKUNNU','','KASARAGOD',671318,9898959697,858287747170,'ramendran@gmail.com','2022-06-14 (1)_Cadaz7v.png',4,31),
(14,'ADIDEV','K','M K HOUSE','KANDOTH','','KASARAGOD',671317,7845961237,89745612356,'adidev@gmail.com','2022-06-14 (2)_E0fbl4r.png',4,32),
(15,'GOUTHAM','G','SAISIVAM','MALAMKUNNU','','KASARAGOD',671318,9963920152,858285828183,'goutham@gmail.com','2022-06-14_rxEq8p8.png',4,33),
(16,'VARUN','B','RAGASUDHA','MALAMKUNNU','','KASARAGOD',671318,8584862135,895848718523,'varunb@gmail.com','Screenshot 2022-07-05 194434_DyP3Rj6.png',4,35);

/*Table structure for table `templeapp_program` */

DROP TABLE IF EXISTS `templeapp_program`;

CREATE TABLE `templeapp_program` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `program` varchar(100) NOT NULL,
  `guest` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_program` */

insert  into `templeapp_program`(`id`,`program`,`guest`,`date`,`time`,`photo`) values 
(2,'GEETHAKNANJAM','SREEDHARAN NAIR  ','2022-07-14','11:30:00.000000','Screenshot (33).png'),
(5,'SAPTHAHAM','NARAYANAN ','2022-07-25','14:30:00.000000','2022-06-14 (2).png');

/*Table structure for table `templeapp_user` */

DROP TABLE IF EXISTS `templeapp_user`;

CREATE TABLE `templeapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `fathers_name` varchar(100) NOT NULL,
  `house_name` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `aadhar_number` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `login_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_user_login_id_id_4b948680_fk_templeapp_login_id` (`login_id_id`),
  CONSTRAINT `templeapp_user_login_id_id_4b948680_fk_templeapp_login_id` FOREIGN KEY (`login_id_id`) REFERENCES `templeapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_user` */

insert  into `templeapp_user`(`id`,`first_name`,`last_name`,`fathers_name`,`house_name`,`street`,`post`,`city`,`pin`,`aadhar_number`,`phone`,`email`,`photo`,`login_id_id`) values 
(6,'RISHIKESH','M K','SANOOP  M K','M K HOUSE','KANDOTH','','NILESWARAM',671390,8765432189076,7845961237,'rishikesh@gmail.com','Screenshot 2022-07-05 194334_i7vldna.png',16),
(7,'Raveendran','C','Narayanan C ','CHATHANASSERY','MALAMKUNNU','','KASARAGOD',671313,7868755645342,9898786545,'ravism@gmail.com','Screenshot 2022-07-05 194434.png',17),
(8,'KRISHNAN','T K','KUNJIKANNAN T','THEKKETHIL','KAPPIL','','KASARAGOGOD',671319,8977060500439,7890654321,'krishnan@gmail.com','Screenshot 2022-07-05 194506.png',22),
(9,'Raveendran','C','Narayanan C ','Chathanassery','Malamkunnu','','KASARAGOD',671319,898548512030,9898786545,'ravism@gmail.com','Screenshot 2022-07-05 194506_zyfleNW.png',34),
(10,'SOORAJ','E','BALAKRISHNAN','SOORYODAYAM','ANGAKALARI','','KASARAGOD',671319,874512963021,9859674123,'sooraj@gmail.com','Screenshot 2022-07-05 194334_4WqYhV8.png',36);

/*Table structure for table `templeapp_videos` */

DROP TABLE IF EXISTS `templeapp_videos`;

CREATE TABLE `templeapp_videos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) NOT NULL,
  `video` varchar(100) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_videos` */

insert  into `templeapp_videos`(`id`,`subject`,`video`,`date_time`) values 
(2,'BHARANI MAHOLSAVAM','videoplayback_lRepREA.mp4','2022-06-22 00:00:00.000000'),
(3,'UTSAVAM','videoplayback_UGGcykh.mp4','2022-06-23 00:00:00.000000');

/*Table structure for table `templeapp_winner` */

DROP TABLE IF EXISTS `templeapp_winner`;

CREATE TABLE `templeapp_winner` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `chitti_id_id` bigint NOT NULL,
  `member_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `templeapp_winner_chitti_id_id_f0164eac_fk_templeapp_chitti_id` (`chitti_id_id`),
  KEY `templeapp_winner_member_id_id_956cf04f_fk_templeapp_members_id` (`member_id_id`),
  CONSTRAINT `templeapp_winner_chitti_id_id_f0164eac_fk_templeapp_chitti_id` FOREIGN KEY (`chitti_id_id`) REFERENCES `templeapp_chitti` (`id`),
  CONSTRAINT `templeapp_winner_member_id_id_956cf04f_fk_templeapp_members_id` FOREIGN KEY (`member_id_id`) REFERENCES `templeapp_members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templeapp_winner` */

insert  into `templeapp_winner`(`id`,`date`,`chitti_id_id`,`member_id_id`) values 
(1,'2022-06-23',4,3),
(2,'2022-06-23',4,4),
(3,'2022-07-23',4,3),
(4,'2022-07-23',4,5);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
