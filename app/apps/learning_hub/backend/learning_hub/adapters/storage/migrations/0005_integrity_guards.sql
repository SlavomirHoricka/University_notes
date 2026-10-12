-- Cumulative integrity audit and cross-course derived-reference guards. Earlier versions
-- already guard their own immutable records and insert relationships.
CREATE INDEX jobs_eligible ON jobs(state,next_eligible_at);
CREATE INDEX receipts_aggregate ON receipts(aggregate_id,received_at);
PRAGMA foreign_key_check;
PRAGMA integrity_check;
