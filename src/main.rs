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


/// Handles the user calling the start command
fn handle_start(args: &ArgMatches) {
    // Get the directory or set it to the default (current working dir) if there is not
    let project_dir = match args.get_one::<PathBuf>("dir") {
        Some(dir) => dir.to_owned(),
        None => env::current_dir().unwrap()
    };

    // First, check if the directory exists
    match project_dir.exists() {
        // If it does, check if it is a directory
        true => match project_dir.is_dir() {
            // If it is a directory, all good
            true => (),
            // If it isn't, print an error and return
            false => {
                eprintln!("Could not start grade book at provided path. Path is not a directory");
                return
            }
        },
        // If it doesn't, create it
        false => fs::create_dir(&project_dir).expect("Failed to create directory to start grade book")
    }

    // Now dir points to an actual directory guaranteed
    // First check if a .grade directory already exists in the dir

    // Get a path that points to the .grade directory
    let grade_dir = project_dir.join(".grade");
    // If it exists and is a directory, exit because the book is already started
    // If it exists and isn't a directory throw an error
    if grade_dir.exists() {
        if !grade_dir.is_dir() {
            eprintln!("Failed to start grade book. {} is not a directory", grade_dir.display());
            return
        }
        println!("Grade book already initialized");
        return
    }

    // If it doesn't exist, the grade book needs to be started

    // In the project directory, create the .grade directory and the .gradeignore file
    fs::create_dir(grade_dir).expect("Failed to create .grade directory");
    // If the .gradeignore doesn't already exist, create an empty one
    let ignore_file = project_dir.join(".gradeignore");
    File::create(ignore_file).expect("Error when attempting to create .gradeignore file");
}

/// Handles the user calling the submit command
fn handle_submit(args: &ArgMatches) {
    //TODO
    println!("Submit called with: ");
    println!("{:?}", args)
}