# Git Bundle Plus

Bundle a local git project with all uncommitted changes, unstaged files, and stashes (git bundle on steroids).

## Contents
- [Requirements](#req)
- [Installation](#inst)
- [Usage](#usage)
- [Example](#ex)
- [**.bundle** output + retrieve git project](#output)
- [How it works](#works)
- [Like](#love)
- [Contributers](#con1)
- [Contribute](#con2)
- [License](#lice)

<a name="req"></a>
## Requirements ✅
* Python 3

<a name="inst"></a>
## Installation 🔌

### Using pip
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Git-Bundle-Plus](https://pypi.org/project/Git-Bundle-Plus/).

```bash
pip install git-bundle-plus
```
### Clone + Python 3 
```bash
git clone https://github.com/an23lm/GitBundlePlus.git
```
```bash
python ./gitbundleplus [-h] path
```

<a name="usage"></a>
## Usage 👩‍💻

```bash
gitbundleplus [-h] path
```
**-h** : Help

**path** : Path to local git project folder you would like to bundle

##### ⚠️ Note: After using `gitbundleplus` on a project the uncommitted and unstaged files will be statshed. You can easily retrieve these files by using `git stash apply` and drop the applied stash with `git stash drop` if you have no further need for it.


<a name="ex"></a>
## Example 👶

### Bundle project
```bash
gitbundleplus ~/Documents/mygitproject
```

### Unbundle project
```bash
git clone ~/Documents/mygitproject.bundle
```

### Retrieve uncommited and unstanged changes
```bash
git stash apply ga-stash-tag-{ga-latest}
```

<a name="output"></a>
## `.bundle` output + retrieve git project 📦
`<git-folder-name>.bundle` will be created in the git folder specified.

### To unbundle the bundled git project, clone the bundle.
```bash
git clone path/to/bundle
```

### Restore the unstaged and uncommitted changes.

All the unstaged and uncommitted changes are stashed (`git stash`) and tagged (`git tag`) before bundling.

```bash
git stash apply ga-stash-tag-{ga-latest}
```

Delete the tag to drop the stash after your done applying.
```bash
git tag -d <tag-name>
```

### Find and apply your previously stashed changes.

`git tag list` to view all your previously stashed changes, tagged with the pattern `ga-stash-tag-{<stash-number>}`. Apply and drop these tagged stashes as per your requirements.
```bash
git stash apply <tag-name>
```
Delete the tag to drop the stash after your done applying.
```bash
git tag -d <tag-name>
```

##### ⚠️ Note: Unbundled projects do not checkout to your current working branch. They default to `master` branch. Please, take care to use `git checkout <branch-name>` to start using a particular branch before applying stashed changes.

#### Please read [How it works](#works) for more information.

<a name="works"></a>
## How it works ⚙️
1. `git stash list` is run and all the previously stashed items are tagged with the pattern `ga-stash-tag-{<stash-number>}`. *Example: `git tag ga-stash-tag-{0} stash@{0}`*.
2. Stash uncommited and unstaged changed using `git stash -u`. If a stash is created, this stash will be assigned the tag `ga-stash-tag-{ga-latest}`.
3. Bundle the git project using `git bundle <git-folder-name>.bundle` and the bundle is placed in the git folder.
4. All the tags from the original git project will be removed. *Example: `git tag -d ga-stash-tag-{0}`*.

<a name="love"></a>
## Show some love ❤️ 
If you found this interesting or helpful, leave a star. ⭐️ 

<a name="con1"></a>
## Contributers 👨‍👩‍👧‍👦
* [Anselm Joseph](https://github.com/an23lm)

<a name="con2"></a>
## Contribute 💪 
Pull requests are welcome.

<a name="lice"></a>
## License 📃 
[MIT](https://choosealicense.com/licenses/mit/)
