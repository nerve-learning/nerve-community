use nerve_file_watcher::{nerve, start_sender};
use std::{
    fs::{self, File},
    io::Write,
    time::Duration,
};

const TEST_DIR: &str = "./exampleFolder";

fn create_file(file_name: &str) -> std::io::Result<()> {
    File::create(TEST_DIR.to_string() + "/" + file_name)?;

    Ok(())
}

fn append_file(file_name: &str, content: &str) -> std::io::Result<()> {
    let file = File::options()
        .append(true)
        .open(TEST_DIR.to_string() + "/" + file_name)?;

    writeln!(&file, "{content}")?;
    Ok(())
}

fn delete_file(file_name: &str) -> std::io::Result<()> {
    fs::remove_file(TEST_DIR.to_string() + "/" + file_name)?;

    Ok(())
}

#[tokio::test]
async fn test1() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let monitor = nerve::make_client("Monitor").await?;

    start_sender(TEST_DIR).await?;
    monitor
        .listen(|ev| println!("{:?}", ev["payload"]), None)
        .await;

    create_file("test.txt")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    // English, Español, Portugues
    append_file("test.txt", "Hello, Hola, Ola")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    delete_file("test.txt")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    println!("\n");
    Ok(())
}

#[tokio::test]
async fn test2() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let monitor = nerve::make_client("Monitor").await?;

    start_sender(TEST_DIR).await?;
    monitor
        .listen(|ev| println!("{:?}", ev["payload"]), None)
        .await;

    create_file("test.txt")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    create_file("best.txt")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    append_file("best.txt", "Hello, Hola, Ola")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    delete_file("best.txt")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    delete_file("test.txt")?;
    tokio::time::sleep(Duration::from_millis(800)).await;

    println!("\n");
    Ok(())
}
