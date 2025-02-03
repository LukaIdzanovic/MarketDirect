# Software Requirements Specification (SRS)


# **MarketDirect**


## 1. Introduction

### 1.1 Purpose
The purpose of this document is to provide a Software Requirements Specification (SRS) for
the development of "MarketDirect" a grocery ordering system which enables users to order
groceries from supermarkets or small local stores. This system is intended to simplify the
process of buying groceries with the purpose to view and manage orders in real-time, and
assist small businesses in expanding their operations through a digital sales channel.

### 1.2 Document Conventions
This document is structured following the IEEE 830-1998 standard for software requirements
specifications. It encompasses user, system, and administrative requirements essential for the
completion of the project.

### 1.3 Intended Audience and Reading Suggestions
This document is designed for developers and designers involved in the project. It is
recommended to read the document from the beggining to gain a full understanding of the
system’s scope and requirements.

### 1.4 Product Scope
The grocery ordering system will be a platform that connects users with local stores and
supermarkets, offering an intuitive way to browse products and place orders. The system will
enhance the local economy by providing small businesses with tools for inventory
management and ordering.

### 1.5 References
 - IEEE 830-1998: IEEE Standard for Software Requirements Specifications (IEEE, 1998).
 - Django Documentation.

## 2. Overall Description

### 2.1 Product Perspective
The system is a web application which features user-friendly interfaces for different user
types (customers, vendors, administrators).

Customers can order fresh groceries from different stores using cryptocurrency tokens for payment purposes.
Vendors control what is being offered and how much it costs, as well as a description and a
picture of the product with the ability to add or remove products. They also manage the
inventory of the online store. In addition to that, vendors have an insight into all orders.
Administrators manages vendors and can see into each vendors statistics (profit and amount
of products sold). Administrator sets the maximum allowed price for each product.

### 2.2 Product Functions

#### User Functions:
o Browse stores and products.
o Place and manage orders.
#### Vendor Functions:
o Manage product inventory and pricing.
o Add and remove products
#### Administrator Functions:
o Manage users and vendors.
o View sales analytics
o Set price for product

### 2.3 User Classes and Characteristics

#### 2.3.1 Customers
Customers can browse products and place orders.

#### 2.3.2 Vendors
Vendors manage their listings, orders, and prices.

#### 2.3.3 Administrators
Administrators oversees all operations.

### 2.4 Operating Environment
The web application will be hosted on a web server, accessible through a web browser.

### 2.5 Design and Implementation Constraints
The web application will be written in Python using the Django framework. It
will be hosted on a web server. The data will be stored in a SQLite database.
No further design and implementation constraints are known at this time.

### 2.6 User Documentation
No documentation will be provided to users.

### 2.7 Assumptions and Dependencies
The application will use a cryptocurrency token to handle payments. For the
first version of the application, the amounts of tokens each user have will be
recorded as a field in the database and will be managed by admin users. The token deposit and
withdrawal functionality will not be implemented in this version of the application.
The application will not have an automated quality assurance process.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Requirements
 - Login: Users can log in to access personalized features.
 - Product Browsing: Users can browse products.
 - Order Placement: Users can add products to a cart and complete the checkout process.

#### 3.1.2 Vendor Requirements
 - Inventory Management: Vendors can add and remove product listings.
 - Order Management: Vendors can view orders.

#### 3.1.3 Administrator Requirements
 - User Management: Admins can add or delete accounts.
 - Apply a Token Balance to a User

## 4. System Interfaces

### 4.1 User Interfaces
The application will feature distinct dashboards for customers, vendors, and administrators,
each tailored to their respective needs. The interface will prioritize ease of use and accessibility.

### 4.2 Software Interfaces
The application will use Django 4.0, the database will be SQLite, frontend framework will be
Bootstrap

### 4.3 Hardware Interfaces
The application will be hosted on a secure web server running on Linux or Windows.

### 4.4 Communication Interfaces
The application will have a secure communication interface for secure data transfer