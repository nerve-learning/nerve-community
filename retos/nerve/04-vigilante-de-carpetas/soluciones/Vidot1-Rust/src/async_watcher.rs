use std::path::Path;

use notify::{self, Config, Event, RecommendedWatcher, Watcher};
use tokio::sync::mpsc::{Receiver, channel};

/// Creates a channel already configured to send events through an async channel
pub fn create() -> notify::Result<(RecommendedWatcher, Receiver<Result<Event, notify::Error>>)> {
    // Esp:
    // Esta implementacaion usa channels de `tokio::sync::mpsc`
    // para poder procesar eventos de `notify` de forma aynchronica
    //
    // Eng:
    // This implementation uses channels from `tokio::sync::mpsc`
    // to be able to process events from `notify` asynchronously
    //

    let (sen, rec) = channel(20);
    let handle = tokio::runtime::Runtime::new()?;

    // Esp:
    // Se usa `handle.block_on` para forzar al sender a
    // ejecutarse de forma syncronica dentro del closure
    //
    // Eng:
    // `handle.block_on` is used to force the sender
    // to execute synchronously inside the closure
    //
    let watcher = RecommendedWatcher::new(
        move |event: Result<Event, notify::Error>| {
            match handle.block_on(async { sen.send(event).await }) {
                Ok(_) => {}
                Err(e) => {
                    eprintln!("{e}");
                }
            };
        },
        Config::default(),
    )?;

    Ok((watcher, rec))
}

/// Starts watching changes in `path` and sends all events to the given `callback`
/// errors are printed on terminal but ignored
pub async fn watch<F>(path: String, callback: F) -> notify::Result<()>
where
    F: Fn(Event),
{
    let (mut watcher, mut receiver) = create()?;
    watcher.watch(
        Path::new(&path.to_string()),
        notify::RecursiveMode::NonRecursive,
    )?;

    println!("Started watching events on {}", path);
    while let Some(res) = receiver.recv().await {
        match res {
            Ok(event) => callback(event),
            Err(err) => eprintln!("watch error: {:?}", err),
        }
    }

    Ok(())
}
