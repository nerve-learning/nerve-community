use nerve_file_watcher::start_sender;
use std::time::Duration;
use tokio::time::sleep;
use std::env;

/*
 * Output:
 * Tipo de evento - Ruta
*/
mod async_watcher;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {

    // Getting commands line arguments
    let args: Vec<String> = env::args().collect();

    // As we all should know, the first arg is always the binary path
    if args.len() != 2 {
        println!("Usage: cargo run <path>");
        return Ok(());
    }

    start_sender(&args[1].to_string()).await?;
    println!("Press Ctrl+C to exit...");
    loop {
        sleep(Duration::from_millis(400)).await;
    }
}
