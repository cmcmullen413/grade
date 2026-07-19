use std::env;
use std::fs::{self, File};
use std::path::{PathBuf};
use clap::{command, Arg, ArgMatches, Command, builder::ValueParser};

fn main() {
    // Define and get the command line arguments and commands
    let matches = command!()
        // Help message about the program itself
        .about("TODO Description about the program")
        // Prints the help message by default if no arguments are supplied
        .arg_required_else_help(true)
        // Command to initialize the grade book
        // By default, it initializes to the current directory
        .subcommand(
            Command::new("start")
                // Git name for this command
                .alias("init")
                // Description of this command
                .about("Starts an empty grade book or restarts an old one")
                // Optional Positional arg
                // If provided, the new grade book is started in the specified subdirectory
                // If it does not already exist, a new directory is created
                .arg(
                    Arg::new("dir")
                        .help("(Optional) The directory to initialize the grade book in")
                        // Specify that the passed value should be a path
                        .value_parser(ValueParser::path_buf())
                        .required(false)
                )
        )
        // Command to create a new submit with the current changes
        .subcommand(
            Command::new("submit")
                // Git name for this command
                .alias("commit")
                // Arg for passing a message directly instead of opening a text editor
                .arg(
                    Arg::new("message")
                        .short('m')
                        .long("message")
                )
        )
        .get_matches();

    // Depending on which subcommand was used, call the correct function with its arguments
    match matches.subcommand() {
        Some(("start", args)) => handle_start(args),
        Some(("submit", args)) => handle_submit(args),
        _ => ()
    }
}

// Command handling functions

/// Handles the user calling the start command
fn handle_start(args: &ArgMatches) {
    // Get the directory or set it to the default (current working dir) if there is not
    let project_dir = match args.get_one::<PathBuf>("dir") {
        Some(dir) => dir.to_owned(),
        None => env::current_dir().unwrap()
    };

    // Use is_book to check if it already is a grade book
    // If it isn't this will also give the error code to know why not
    let code = is_book(&project_dir);

    // If code == 0, then the directory is already a book
    if code == 0 {
        println!("Grade book already exists");
        return
    }

    // If code == -2, the path is not a directory
    if code == -2 {
        eprintln!("Could not start grade book at provided path. Path is not a directory");
        return
    }

    // If code == 2, the .grade path is not a directory
    if code == 2 {
        eprintln!("Failed to start grade book. Path to .grade is not a directory");
        return
    }

    // If code == -1 or 1, the directory does not exist yet or the .grade directory does not exist yet
    //  so attempt to create the one(s) that don't exist yet
    if code == -1 || code == 1 {
        fs::create_dir_all(project_dir.join(".grade")).expect("Failed to create one or more directories when starting grade book");
        // Now if the .gradeignore doesn't exist, create that
        let ignore_path = project_dir.join(".gradeignore");
        if !ignore_path.exists() {
            File::create(ignore_path).expect("Failed to create .gradeignore file");
        }
    }
}

/// Handles the user calling the submit command
fn handle_submit(args: &ArgMatches) {
    //TODO
    println!("Submit called with: ");
    println!("{:?}", args)
}

// Helper Functions

/// Checks whether the passed in directory is a grade book or not
/// Returns 0 on true and different integers on false depending on the reason
///
/// -1  ->  Provided path does not exist
///
/// -2  ->  Provided path is not a directory
///
///  1  ->  dir/.grade does not exist
///
///  2  ->  dir/.grade is not a directory
fn is_book(dir: &PathBuf) -> i8 {
    // Check if the path exists
    if !dir.exists() { return -1 }
    // And is a directory
    if !dir.is_dir() { return -2 }

    // Get the path that should point to the .grade directory
    let grade_dir = dir.join(".grade");

    // Check if the .grade path exists
    if !grade_dir.exists() { return 1 }
    // And is a directory
    if !grade_dir.is_dir() { return 2 }

    // Otherwise return true
    0
}