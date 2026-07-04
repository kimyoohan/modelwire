@echo off
rem FactQuire outreach dispatch: send queued items in the US-morning window.
rem Registered in Windows Task Scheduler as "FactQuire Outreach Send" (Tuesdays 23:00 KST).
cd /d "E:\0.세계1등기업\modelwire"
echo ===== %date% %time% OUTREACH DISPATCH (claude) =====
call "C:\Users\USER\AppData\Roaming\npm\claude.cmd" -p --dangerously-skip-permissions "Read SEND_ORDER.md in this directory and execute it fully. Work autonomously until the protocol is complete." >> ops\outreach\dispatch.log 2>&1
echo ===== %date% %time% DONE =====
