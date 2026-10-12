# Personal learning app

This folder is the standalone source package for the local browser-based learning app. It contains its own backend/frontend, engineering plan, agent profiles and maintained workflow sources. It contains no university notes, original course materials, learner records or credentials.

The app is an **unfinished, tested engineering checkpoint**. It has the typed SQLite foundation and responsive course/materials shell. Real uploads, provider integration, learning sessions and the manual launcher remain incomplete. See [current state](docs/learning-hub/CURRENT_STATE.md).

- [Run and inspect the existing shell](apps/learning_hub/README.md)
- [Export this folder and create the new repository](MIGRATION.md)
- [Engineering plan and task graph](docs/learning-hub/START_HERE.md)
- [Workflow source ownership](03_Agents/README.md)

Source layout is retained inside this envelope so build commands, role paths, packaging and plan validation work after copying. The sibling vault is not needed to build/test this checkpoint. The copied academic workflows are a separate maintained fork awaiting an app-owned runtime data-root bridge; they are not enabled against the original notes.
