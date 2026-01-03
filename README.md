# Expense Tracker

A Python-based expense tracking application that helps you manage and analyze your expenses with a user-friendly command-line interface. The application stores data in Supabase (cloud database) and provides visual analytics through charts and graphs.

## Features

- 🔐 **User Authentication**: Secure login and signup with password hashing using bcrypt
- 💰 **Expense Management**: 
  - Add multiple expenses at once
  - View all expenses or filter by category/date range
  - Modify existing expenses
  - Delete expenses with confirmation
- 📊 **Analytics & Reports**:
  - Monthly expense summaries
  - Category-wise expense breakdown
  - Daily expense trends
  - Visual charts (bar charts, pie charts, line graphs)
- 🔍 **Advanced Filtering**:
  - Filter expenses by category
  - Filter expenses by date range
  - View expenses sorted by date

## Prerequisites

- Python 3.7 or higher
- Internet connection (required for Supabase database access)
- Supabase account and project (for database storage)

## Installation

1. **Clone or download this repository**

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install bcrypt matplotlib supabase
   ```

## Configuration

The application is pre-configured with a Supabase database. The connection details are in the script:
- Supabase URL: `https://chctrmjuvctogplzojln.supabase.co`
- API Key: Already configured in the script

**Note**: If you want to use your own Supabase database:
1. Create a Supabase project at [supabase.com](https://supabase.com)
2. Create two tables:
   - `users` table with columns: `id`, `username`, `password`
   - `expenses` table with columns: `user_id`, `amount`, `date`, `description`, `category`
3. Update the `url` and `key` variables in the script with your Supabase credentials

## Usage

### Running the Application

```bash
python "expenses tracking.py"
```

### Getting Started

1. **Sign Up** (if you're a new user):
   - Press `j` to sign up
   - Enter your user ID, name, and password
   - Your password will be securely hashed and stored

2. **Login** (if you have an account):
   - Press `f` to login
   - Enter your user ID, username, and password

3. **Exit**:
   - Press `k` to exit the application

### Main Menu Options

After logging in, you'll see the following options:

1. **Add a new expense record**
   - Enter categories separated by commas (e.g., `electricity, grocery, rent`)
   - For each category, enter:
     - Amount
     - Optional description/note
     - Date (format: `YYYY-MM-DD`)

2. **View stored expenses**
   - View all expenses sorted by date
   - Filter by category (press `c`)
   - Filter by date range (press `d`)
   - Exit view mode (press `e`)

3. **Modify existing expenses**
   - Enter the category and date of the expense to modify
   - Update amount, description, and date

4. **Delete an expense**
   - Enter the category and date of the expense to delete
   - View matching expenses before deletion
   - Confirm deletion (Y/N)

5. **Show monthly summary**
   - Enter year and month
   - View:
     - Total spent
     - Number of expenses
     - Category-wise breakdown
     - Highest expense
     - Visual charts (bar chart, pie chart, line graph)

6. **Exit**
   - Exit the application

## Data Storage

- **Location**: All data is stored in Supabase cloud database
- **Tables**:
  - `users`: Stores user account information
  - `expenses`: Stores all expense records
- **Access**: Data is accessible from any device with internet connection
- **Backup**: Data is automatically backed up by Supabase

## Project Structure

```
Expense-tracking.py-repo/
├── expenses tracking.py    # Main application file
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Dependencies

- `bcrypt`: Password hashing for secure authentication
- `matplotlib`: Creating visual charts and graphs
- `supabase`: Database client for cloud data storage

## Error Handling

- The application includes error handling for invalid inputs
- Errors are logged to `error.log` file (created automatically if errors occur)
- Keyboard interrupt (Ctrl+C) is handled gracefully

## Example Usage

```
--Please login (press "f" to login)
--if your new please sign up (press "j" to sign up)
--In order to exit press 'k'

Enter your choice (login(f) , sign up(j) or exit(k)):- f

Enter your user id:- 1
Enter your name:- John
Enter the password:- ****

******* LOGIN SUCCESSFULL....!!!! *******

What would you like to perform....????

1.) Add a new expense record
2.) View stored expenses
3.) Modify existing expenses
4.) Delete an expense
5.) Show monthly summary
6.) Exit

Enter your choice:- 1
```

## Notes

- Date format: Always use `YYYY-MM-DD` format (e.g., `2024-01-15`)
- Amounts: Enter numeric values (decimals allowed)
- Categories: Case-insensitive, automatically converted to lowercase
- Charts: Charts will open in separate windows using matplotlib

## Security Note

⚠️ **Important**: The Supabase credentials are currently hardcoded in the script. For production use, consider:
- Using environment variables
- Using a `.env` file (and adding it to `.gitignore`)
- Never commit sensitive credentials to version control

## License

This project is open source and available for personal use.

## Support

If you encounter any issues:
1. Check that all dependencies are installed
2. Verify your internet connection
3. Check the `error.log` file for error details
4. Ensure your Supabase database is accessible

---

**Happy Expense Tracking! 💰📊**


