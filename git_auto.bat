
@echo off
setlocal
cd /d "%~dp0"

echo.
echo ===== GitHub Automation =====

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ERROR: This folder is not a Git repository.
    exit /b 1
)

git branch --show-current
git add .
if errorlevel 1 (
    echo ERROR: Could not stage files.
    exit /b 1
)

git diff --cached --quiet
if errorlevel 2 (
    echo ERROR: Could not check staged changes.
    exit /b 1
)

if errorlevel 1 goto commit_changes
echo No new changes to commit.
goto sync

:commit_changes
set "msg="
set /p "msg=Enter commit message: "
if not defined msg set "msg=Python practice update"

git commit -m "%msg%"
if errorlevel 1 (
    echo ERROR: Commit failed. Push cancelled.
    exit /b 1
)

:sync
git pull --rebase origin main
if errorlevel 1 (
    echo ERROR: Pull or rebase failed.
    echo Resolve the issue before running this script again.
    exit /b 1
)

git push -u origin main
if errorlevel 1 (
    echo ERROR: Push failed. Check the message above.
    exit /b 1
)

echo.
echo SUCCESS: GitHub is synchronized.
git status
endlocal