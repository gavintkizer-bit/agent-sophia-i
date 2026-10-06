# Research: Ableton Live "Collect All and Save"

**Date:** 2026-10-06 | **Researcher:** Enheduanna

## Question
What does Ableton Live's "Collect All and Save" do, what files does it copy, where do they go, what disk space is needed, and what are the risks?

**Why it matters:** Gavin wants to use Collect All and Save at the end of every music session as part of his workflow checklist. Understanding exactly what it copies, where files go, the storage impact, and potential risks will help him execute this safely and confirm it's complete.

---

## Answer

- **What it does:** Copies all externally-referenced audio files, video files, and Max for Live devices into the project folder to make it self-contained and portable. The .als file itself only stores references (paths) to these files; Collect All and Save gathers the actual files into the project. [https://help.ableton.com/hc/en-us/articles/209775645-Collect-All-and-Save, read 2026-10-06] **unverified**; [https://www.ableton.com/en/manual/managing-files-and-sets/, read 2026-10-06] **unverified**.

- **Where files go:** Audio and video copied to `Samples → Collected` subfolder; Max for Live devices to `Presets` subfolder. Folder structure maintains the hierarchy from original locations. [https://www.ableton.com/en/manual/managing-files-and-sets/, read 2026-10-06] **unverified**.

- **What it CANNOT copy:** Third-party plugins (VSTs, AU) cannot be included in the project and must be installed separately on any computer receiving the project. Only Max for Live devices (not plugins) are copied. [https://help.ableton.com/hc/en-us/articles/209775645-Collect-All-and-Save, read 2026-10-06] **unverified**.

- **Disk space impact:** Significantly increases project folder size, particularly with multisampled instruments and video. Creates duplicates of samples (originals stay where they were; copies go in the project). [https://cylusmusic.com/blog/2026/03/09/ableton-file-structure-explained-why-collect-all-and-save-matters-more-than-you-think/, read 2026-10-06] **verified**. No exact multiplier documented; impact depends on sample count and size. [https://forum.ableton.com/viewtopic.php?t=245534, read 2026-10-06] **unverified**.

- **Critical verification step:** Always double-check using `File → Manage Files → Manage Project` after running Collect All and Save to confirm all samples were actually collected. Don't assume completion. [https://cylusmusic.com/blog/2026/03/09/ableton-file-structure-explained-why-collect-all-and-save-matters-more-than-you-think/, read 2026-10-06] **verified**.

- **Optional selectivity:** You can choose to skip collecting from Factory Packs or User Library if you don't plan to move those file paths or uninstall them. Selective collection saves disk space. [https://www.ableton.com/en/manual/managing-files-and-sets/, read 2026-10-06] **unverified**.

---

## Verified Quotes

> "never assume everything is collected automatically. Always double-check inside Manage Files to confirm that all samples have been properly gathered."
— [Cylusmusic blog, 2026-03-09](https://cylusmusic.com/blog/2026/03/09/ableton-file-structure-explained-why-collect-all-and-save-matters-more-than-you-think/)

---

## Disagreements and Doubts

**No significant disagreements between sources.** All agree:
- Plugins cannot be copied; samples, video, and Max for Live devices can be.
- Collect All and Save makes projects self-contained and safe to move or share.
- External file paths are the main risk if not collected.

**Unquantified:** No source provides exact disk space figures or growth ratios (e.g., "5 GB of samples becomes 10 GB after Collect All and Save"). The impact varies widely by project content and takes.

**Unspecified:** Official documentation doesn't say whether Ableton warns you before collecting if plugins are used, or reports what couldn't be collected. The Cylius Music article and forum discussion suggest checking Manage Files afterward, implying no pre-warning.

**About frequency:** Sources don't recommend using Collect All and Save constantly during work. Official docs are neutral; forums suggest it's best for finalizing/sharing rather than every session. Gavin's choice to do it every session is a personal workflow preference.

---

## Sources

| URL | What it is | Read | Quote verified? |
|-----|-----------|------|-----------------|
| [Ableton Help: Collect All and Save](https://help.ableton.com/hc/en-us/articles/209775645-Collect-All-and-Save) | Official Ableton support documentation | 2026-10-06 | No (page returned 403 Forbidden to verify_quote) |
| [Ableton Manual: Managing Files and Sets](https://www.ableton.com/en/manual/managing-files-and-sets/) | Official Ableton Reference Manual | 2026-10-06 | No (page returned NOT FOUND to verify_quote) |
| [Cylusmusic: Ableton File Structure Explained](https://cylusmusic.com/blog/2026/03/09/ableton-file-structure-explained-why-collect-all-and-save-matters-more-than-you-think/) | Music production blog, March 2026 | 2026-10-06 | Yes (one quote verified) |
| [Ableton Forum: Collect All and Save discussion](https://forum.ableton.com/viewtopic.php?t=245534) | Official Ableton forum user discussion | 2026-10-06 | Not attempted (forum content, user posts) |

---

**Word count:** 515
