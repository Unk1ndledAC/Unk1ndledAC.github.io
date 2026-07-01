@echo off
setlocal
echo.
echo [1/4] Syncing GitCSTV client page (with front matter)...
REM Build clean front matter + body into target
echo ---> D:\GithubProjects\MyBlog\source\gitcstv\index.html
echo title: GitCSTV>> D:\GithubProjects\MyBlog\source\gitcstv\index.html
echo layout: false>> D:\GithubProjects\MyBlog\source\gitcstv\index.html
echo --->> D:\GithubProjects\MyBlog\source\gitcstv\index.html
type D:\GithubProjects\gitcstv\docs\index.html>> D:\GithubProjects\MyBlog\source\gitcstv\index.html
if %errorlevel% neq 0 (echo ERROR: Failed to sync & exit /b 1)
echo       Done.
echo.
echo [2/4] Cleaning...
hexo clean
echo.
echo [3/4] Generating...
hexo g
if %errorlevel% neq 0 (echo ERROR: hexo g failed & exit /b 1)
echo.
echo [4/4] Deploying...
hexo d
if %errorlevel% neq 0 (echo WARNING: hexo d failed. Check git proxy. & exit /b 1)
echo.
echo ============================================================
echo SUCCESS - https://unk1ndledac.github.io/gitcstv/
echo ============================================================