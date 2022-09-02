# regex for Validation
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
USER_NAME_REGEX = r"^[A-Za-z\d@$!_#%*?&]{3,30}$"
BLOG_TITLE_REGEX = r"^[A-Za-z\d@$!_#%*?& ]{5,30}$"
BLOG_CONTENT_REGEX = r"^[A-Za-z\d@$!_+#%*?& ]{10,10000}$"

# user
MSG_RETRIEVE_USER = "Successfully retrieved user."
ERR_SQL_ALCHEMY_ERROR = "Error in storing database."
MSG_REGISTER_USER_SUCCESSFULLY = "Hey, you registered successfully."
MSG_USER_PROFILE_UPDATED_SUCCESSFULLY = "Profile updated successfully."
MSG_PASSWORD_CHANGED_SUCCESSFULLY = "Your Password Changed Successfully!"
MSG_DELETED_USER = "User deleted successfully."
MSG_LOG_IN_SUCCESSFULLY = "Successfully Logged in."
ERR_PASSWORD_INCORRECT = "Password incorrect."
ERR_USER_WITH_EMAIL_NOT_EXISTS = "There is no user with email {}"
ERR_USER_NOT_EXISTS = "user with is {} is not exsits"
MSG_USER_SAVED_TO_DB_SUCCESSFULLY = "User Saved to Database"
MSG_USER_UPDATED_TO_DB_SUCCESSFULLY = "User Detail Updated Successfully to Database"
MSG_USER_DELETED_FROM_DB_SUCCESSFULLY = "User Deleted from Database"

# token
ERR_NOT_VALID_TOKEN = 'Your Token is Not Valid!'

# for mail
MSG_CHECK_EMAIL_FOR_FURTHER_PROCESS = 'Please check your Registered Email For Further Instruction'
ERR_MAIL_NOT_SEND = 'Failure! Mail Not Sent Successfully!!'

# constants used in blog module
MSG_RETRIEVE_BLOG = "Successfully retrieved blog."
MSG_RETRIEVE_BLOGS = "Successfully retrieved All blogs."
MSG_REGISTER_BLOG_CREATED_SUCCESSFULLY = "Blog created successfully."
MSG_REGISTER_BLOG_UPDATED_SUCCESSFULLY = "Blog updated successfully."
MSG_DELETED_BLOG = "Blog deleted successfully."
MSG_BLOG_SAVED_TO_DB = "Blog Saved to Database"
MSG_BLOG_UPDATED_TO_DB = "Blog Detail Updated To Database"
MSG_BLOG_DELETED_FROM_DB = "Blog Deleted from Database"
ERR_BLOG_NOT_EXISTS = "Blog with blog id {} does not exists."
ERR_NO_BLOG_IN_DB = "NO Blog Available To Display"
ERR_BLOG_NOT_EXISTS_OR_NOT_AUTHENTICATED = "There is no blog available in database or Your Are not Authenticated!"

ERR_INVALID_USERNAME = 'Please Enter Valid Username!, Title Length Must be 3 to 30 and Alphanumeric'
ERR_INVALID_EMAIL = "Please Enter Valid Email Address!"
ERR_INVALID_PASSWORD = "Please Enter valid Password!"
ERR_INVALID_BLOG_TITLE = 'Please Enter Valid Title!, Title Length Must be 5 to 30'
ERR_INVALID_BLOG_CONTENT = "Please Enter Valid content , Length must be between 10 to 10000"

ERR_INVALID_CONFIRM_PASSWORD = 'Your Both Password Should be same!'
