# Learning workflow architecture

Source: [[Drawing 2026-10-03 19.22.41.excalidraw]]

```mermaid
flowchart LR
    Request["User request"] --> Selection{"Agent selects a Uni Learning skill"}
    Selection -.-> Ingest
    Selection -.-> Plan
    Selection -.-> Teach
    Selection -.-> Recall

    Raw["New or changed course materials"] --> Ingest["Ingestion agent<br/>ingest skill · capable model"]
    Ingest -->|creates and checks| Notes["Finished teaching notes<br/>01_Notes"]
    Notes -->|only curriculum source| Plan["Planning agent<br/>plan skill · capable model"]
    Plan -->|creates and revises| Blueprint["Learning plan<br/>objectives, route, rubrics, review prompts"]

    Notes -->|canonical lesson content| Teach["Teaching agent<br/>teach skill · lighter model"]
    Blueprint -->|prepared route| Teach
    Teach -->|observed answers and feedback| Log["Learning log<br/>03_Agents"]

    Blueprint --> Recall["Recall agent<br/>recall skill · lighter model"]
    Log --> Recall
    Recall -->|schedule proposal| Log
    Recall -->|actionable reminder| Learner["Learner"]
    Learner -->|starts review| Teach
```

The planner is the only writer of the learning plan. The teaching agent reads the finished notes and plan, and writes learner evidence to the log. Recall schedules reviews and reminders; only an observed teaching or review session can add learning outcomes. Skill selection follows the request; model selection is a separate host setting.
