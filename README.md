# T3 Team acceptance fixture

This repository contains synthetic query and page examples used to verify
controlled agent collaboration, independent review, defect repair and GitHub CI.
It contains no product source code, account data, credentials or production logs.

The protected `main` branch requires the `acceptance` check. Agents update a
requirement branch and a single draft pull request. Automatic merging is disabled;
the final merge remains a human decision.

The initial skeleton deliberately contains no generated feature implementation.
An initial skeleton check alone does not prove the Team workflow passed.
