@echo off
REM ============================================================
REM GitCSTV Sync & Deploy Script
REM ============================================================
REM Syncs the client-side card generator from the GitCSTV project
REM into the Hexo blog, rebuilds, and deploys to GitHub Pages.
REM
REM Source: D:\GithubProjects\gitcstv\docs\index.html
REM Target: D:\GithubProjects\MyBlog\source\gitcstv\index.html
REM ============================================================

echo.
echo [1/4] Syncing GitCSTV client page...
copy /Y "D:\GithubProjects\gitcstv\docs\index.html" "D:\GithubProjects\MyBlog\source\gitcstv\index.html"
if errorlevel 1 (
    echo ERROR: Failed to sync. Check that GitCSTV project exists.
    exit /b 1
)
echo       Done.

echo.
echo [2/4] Cleaning previous build...
call hexo clean
if errorlevel 1 (
    echo ERROR: hexo clean failed.
    exit /b 1
)

echo.
echo [3/4] Generating static site...
call hexo g
if errorlevel 1 (
    echo ERROR: hexo g failed.
    exit /b 1
)

echo.
echo [4/4] Deploying to GitHub Pages...
call hexo d
if errorlevel 1 (
    echo.
    echo ============================================================
    echo WARNING: hexo d may have failed due to network/auth issues.
    echo Try setting git proxy first:
    echo   git config --global http.proxy http://127.0.0.1:7890
    echo   git config --global https.proxy http://127.0.0.1:7890
    echo Then re-run: hexo d
    echo ============================================================
    exit /b 1
)

echo.
echo ============================================================
echo SUCCESS — Deployed to https://unk1ndledac.github.io/gitcstv/
echo ============================================================
