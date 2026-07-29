use nerve_file_watcher::start_sender;
use std::time::Duration;
use tokio::time::sleep;

/*
 * Output:
 * Tipo de evento - Ruta
*/
mod async_watcher;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    start_sender(&"./exampleFolder".to_string()).await?;

    println!("Press Ctrl+C to exit...");
    loop {
        sleep(Duration::from_millis(400)).await;
    }
}
