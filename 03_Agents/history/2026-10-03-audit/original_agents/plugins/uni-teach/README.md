# University Assistant

Private skills-only plugin for the local Uni Obsidian vault. The plugin keeps the existing technical identity uni-teach and now offers four skills.

| Ask for | Skill | Preferred model |
|---|---|---|
| Ingest new or changed course material and create finished notes | ingest | Highly capable |
| Create or revise the learning plan after notes change | plan | Highly capable |
| Learn, practise, revise, or resume a topic | teach | Lighter and faster |
| See due topics or prepare spaced review reminders | recall | Lighter and faster |

The model chooses a skill from its description and the user's request. A skill cannot itself switch the host model. Select the desired model for the planning or study session. The plugin uses the vault's existing files and requires local read/write access; it has no MCP server or remote vault connection.

Ownership: ingest alone writes 01_Notes, plan alone writes learning_plan.md and source_manifest.md, teach records actual learner answers in learning_log.md, and recall adds schedule proposals or reminders. A due review never counts as demonstrated learning. See LEARNING_ARCHITECTURE.md for the workflow and SM-2-style interval baseline.

The original standalone ingest and teach skills remain in 03_Agents/ingest and 03_Agents/teach. Their current versions are copied into this plugin; new plan and recall source skills live beside them. Course notes, raw materials, ingestion logs, and learner records are not packaged. Installing this plugin on a host without the local Uni vault does not grant vault access.

The private plugin's account release is updated from this source package. plugin.json is the portable manifest; .codex-plugin/plugin.json is the synchronized Codex compatibility manifest.
