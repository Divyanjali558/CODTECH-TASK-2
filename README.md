**Name:** Gannamaneni Divyanjali

**ID:** CT6FS1021

**Company:** CODTECH IT SOLUTIONS Pvt Ltd

**Domain:** FULL STACK

**Duration:** JULY 5th, 2024 to AUGUST 20th, 2024

**Mentor:** Neela Santhosh Kumar



## Project Overview

**Project Description**

**Features**

**User Authentication:**

**Registration:** 

Users can create an account by providing their email, password, and username.

**Login:** 

Registered users can log in to access their personal dashboard and manage their recipes.

**JWT Security:**

User sessions are managed using JSON Web Tokens (JWT), ensuring secure authentication and authorization.

**Recipe Management:**

**Create Recipes:**

Users can add new recipes by providing details such as title, ingredients, steps, and images.

**View Recipes:**

Users can browse all available recipes or view details of a specific recipe.


**Update Recipes:**

Users can edit their recipes to update ingredients, instructions, or other details.

**Delete Recipes:** Users can remove recipes they no longer want to keep.

**User Interface:**

**Responsive Design:** The platform is optimized for both desktop and mobile devices.


**Easy Navigation:**

A clear and simple navigation structure to enhance user experience.


**Modern UI:**

Utilizes modern UI frameworks to provide a clean and visually appealing interface.

## Technology Stack
**Frontend:** React.js

**React Router:** For handling route navigation within the app.

**Axios:** For making HTTP requests to the backend API.

**JWT-decode:** For decoding JWT tokens and managing user sessions on the client side.

**Backend:** Express.js

**Mongoose:** For interacting with MongoDB, the chosen database.

**Bcryptjs:** For hashing passwords before storing them in the database.

**JWT:** For creating and verifying JSON Web Tokens for user authentication.

**Dotenv:** For managing environment variables securely.

**Database:** MongoDB

**Atlas:** MongoDB Atlas is used for hosting the database, providing a reliable and scalable cloud database solution.

## Project Structure
**Backend:**

**Controllers:** Manage the business logic for users and recipes.

userController.js

recipeController.js

**Models:** Define the schema for users and recipes.

userModel.js

recipeModel.js

**Routes:** Define API endpoints for user and recipe operations.

userRoutes.js

recipeRoutes.js

**Middleware:** Contains middleware functions for authentication and error handling.

authMiddleware.js

**Utils:** Utility functions for generating tokens.

generateToken.js

**Main Server File:** server.js – entry point of the backend application.

**Frontend:**

**Components:** Reusable UI components.

Header.js

RecipeForm.js

RecipeList.js

RecipeDetails.js

**Pages:** Define different pages of the application.

Home.js

Register.js

Login.js

Recipe.js

**Main App File:** App.js – root component that sets up routes and renders other components.

**Entry Point:** index.js – entry point of the React application.

## Installation and Setup

**Backend:**

Navigate to the backend directory.

Run **npm install** to install dependencies.

Create a **.env file** with the following variables

Start the server with **npm start**

**Frontend:**

Navigate to the frontend directory.

Run **npm install** to install dependencies.

Ensure the public directory contains **index.html** and the src directory contains **index.js**.

Start the development server with **npm start**.

![Screenshot 2024-07-29 101159](https://github.com/user-attachments/assets/eb0e21b1-be42-42cd-863b-d22044506cce)

![Screenshot 2024-07-21 114900](https://github.com/user-attachments/assets/c21a9e6d-1d5a-4c3a-91f7-a6324af73704)



## Conclusion
The Recipe Sharing Platform provides a comprehensive solution for users to share and manage recipes. With a robust backend, secure authentication, and a responsive frontend, it offers an excellent user experience. This project can be further extended with additional features such as user profiles, search functionality, and social sharing.
