> **Before submitting the PR**
>
> - Fill in and tick fields
> - _Remove all rows_ that are not relevant for the current PR
>   - Revelant option missing? Add it as an item and add a PR comment informing that the new option should be included into this template.
>
> **All _relevant_ items should be ticked before the PR is merged**

# Description

- [ ] Summary of the changes and the related issue:
- [ ] List / description of any dependencies or other changes required for this change:
- Fixes an issue in GitHub / Jira:
  - [ ] Yes: _[link to GitHub issue / Jira task ID]_
  - [ ] No

## Type of change

- [ ] Bug fix
  - [ ] Breaking: _Describe_
  - [ ] Non-breaking
- [ ] Documentation
- [ ] New feature
  - [ ] Breaking: _Describe_
  - [ ] Non-breaking
- [ ] Security Alert fix
- [ ] Tests **(only)**
- [ ] Workflow

_"Breaking": The change will cause existing functionality to not work as expected._

# Checklist:

## General

- [ ] [Changelog](../CHANGELOG.md): New row added. Not needed when PR includes _only_ tests.
- [ ] Code change
  - [ ] Self-review of code done
  - [ ] Comments added, particularly in hard-to-understand areas
  - Documentation update
    - [ ] Done
    - [ ] Not needed

## Repository / Releases

- [ ] Blocking PRs have been merged
- [ ] Rebase / update of branch done
- [ ] PR to `master` branch (Product Owner / Scrum Master)
  - [ ] I have followed steps 1-5 in [the release instructions](../docs/procedures/new_release.md)
  - [ ] I am bumping the major version (e.g. 1.x.x to 2.x.x)
  - [ ] I have made the corresponding changes to the API version

## Checks

- [ ] CodeQL passes
- [ ] Formatting: Black & Prettier checks pass
- Tests
  - [ ] I have added tests for the new code
  - [ ] The tests pass
- Trivy:
  - [ ] There are no new security alerts
  - [ ] This PR fixes new security alerts
  - [ ] Security alerts have been dismissed
  - [ ] PR will be merged with new security alerts; This is why: _Please add a short description here_
