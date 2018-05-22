===============
Release Process
===============

The easiest way to release a new version of moleculerize is to use make.

1. First you will need to know the username and password for the account you want to use to release to PyPI shared_accounts_

2. You will need to make sure that you are on the master branch, your working directory is clean and up to date.

3. Decide if you are going to increment the major, minor, or patch version.  You can refer to semver_ to help you make that decision.

4. Use the `release-major`, `release-minor`, or `release-patch`.

**make release** ::

    make release-minor
5. The task will stop and prompt you for you PyPI username and password if you dont have these set in your `.pypirc` file.

6. Once the task has successfully completed you need to push the tag and commit.

**push tag** ::

    git push origin && git push origin refs/tags/<tagname>
7. Create a release on GitHub. GitHub_release_

.. _semver: https://semver.org
.. _shared_accounts: https://rpc-openstack.atlassian.net/wiki/spaces/ASC/pages/143949893/Useful+Links#UsefulLinks-SharedAccounts
.. _GitHub_release: https://help.github.com/articles/creating-releases/
