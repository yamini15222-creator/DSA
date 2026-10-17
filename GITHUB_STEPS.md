# Push this project to GitHub

## 1. Open a terminal in the project folder

In Windows File Explorer, open the `Day-01-to-40-DSA` folder, click the address bar, type `cmd`, and press Enter.

Alternatively, in VS Code choose **File → Open Folder**, open this folder, then choose **Terminal → New Terminal**.

## 2. Run the code and tests

```bash
python main.py
python -m pip install pytest
python -m pytest -v
```

Fix any failing tests before uploading.

## 3. Initialize Git

Run these commands from inside the `Day-01-to-40-DSA` folder:

```bash
git init
git add .
git commit -m "Add Days 1-40 DSA revision solutions"
```

If Git asks you to configure your identity, use the name and email you want associated with your commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Then run the commit command again.

## 4. Create a GitHub repository

1. Sign in at https://github.com/
2. Click **New repository**.
3. Name it `Day-01-to-40-DSA`.
4. Choose Public or Private.
5. For this workflow, create it without adding a README, license, or `.gitignore`, because this folder already has project files.
6. Create the repository and copy its HTTPS repository URL.

## 5. Connect and push

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Day-01-to-40-DSA.git
git push -u origin main
```

If Git says `origin` already exists, use this instead:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/Day-01-to-40-DSA.git
git push -u origin main
```

Follow GitHub's sign-in or authentication prompts. Do not put your password or token directly into source code.

## 6. Later, after editing files

```bash
git add .
git commit -m "Improve DSA solutions and tests"
git push
```

## What the Git commands mean

- `git init`: start tracking the folder with Git.
- `git status`: show changed and untracked files.
- `git add .`: stage the current changes.
- `git commit -m "message"`: save a local snapshot with a description.
- `git branch -M main`: name the current branch `main`.
- `git remote add origin URL`: connect the local repository to GitHub.
- `git push -u origin main`: upload the branch and set its upstream.
- `git pull`: fetch and integrate remote changes.
