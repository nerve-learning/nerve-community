mod async_watcher;
pub mod nerve;

pub async fn start_sender(path: &str) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let watcher_client = nerve::make_client("FileWatcher").await?;

    tokio::spawn(async_watcher::watch(path.to_string(), move |ev| {
        // Por los momentos, simplemente imprime el error
        // ya en un futuro veo como loegear mis cosas
        let val = match serde_json::to_value(ev) {
            Ok(v) => v,
            Err(e) => {
                eprintln!("{e}");
                return;
            }
        };

        // Pudiera manejar este error
        // pero realmente si falla tampoco va a crashear el programa
        let _ = watcher_client.send("Monitor", val);
    }));

    println!("Watcher created successfully!");
    Ok(())
}
