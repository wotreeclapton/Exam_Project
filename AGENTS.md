# Exam Application - Development Instructions

## Project Overview

This is a Windows classroom examination application written in Python.

The original application was created in approximately 2019 and is now
being gradually refactored and improved.

The GUI currently uses PyQt5.

The application is used on student PCs in a school computer room.

## Important Principle

Refactor incrementally.

Do not rewrite the whole application unless specifically requested.

Existing working behaviour should be preserved while individual parts
are improved.

## Current Application Features

The application:

- Allows students to log in using their given name and password.
- Connects to a classroom server.
- Loads multiple-choice examinations.
- Supports text, images and video in questions and answers.
- Randomizes question order.
- Has a countdown timer.
- Prevents multiple instances of the application.
- Detects whether a student has already attempted an examination.
- Records the student's score.
- Records which questions were answered correctly or incorrectly.

## Planned Changes

The existing shared Excel results file will be removed.

A safer results-storage system will replace it because multiple student
computers may attempt to write results simultaneously.

The application will eventually be packaged as a Windows executable
using PyInstaller and distributed using an installer that supports
future updates.

## Coding Guidelines

- Prefer clear, readable Python over clever or highly compressed code.
- Use descriptive variable and function names.
- Add type hints where they improve clarity.
- Keep GUI code separate from exam logic where practical.
- Keep server/network access separate from GUI logic where practical.
- Keep result storage separate from exam logic.
- Avoid unnecessary dependencies.
- Do not change existing behaviour unless specifically requested.
- When refactoring, make small changes that can be tested individually.
- Explain significant architectural changes before implementing them.
- Preserve compatibility with Windows unless explicitly told otherwise.

## Safety

This software is used for real student examinations.

Changes affecting:

- student authentication
- exam attempt detection
- result storage
- timers
- question selection
- scoring

should be treated as sensitive functionality.

Do not silently change their behaviour.

## Working Style

Before making a substantial change:

1. Identify the relevant existing code.
2. Explain the proposed change.
3. Make the smallest reasonable change.
4. Check for affected code elsewhere in the project.
5. Test or describe how the change should be tested.

## Known Legacy Architecture

The original application has a large App class in exam_app_main.py.

It currently handles:

- GUI control
- network authentication
- student authentication
- exam loading
- question state
- scoring
- timers
- multimedia
- attempt detection
- result persistence

This class should eventually be decomposed, but only incrementally.

## Known Legacy Assumptions

The existing application currently relies on several assumptions that
should not be changed without investigation:

- Student numbers may correspond directly to combo-box indexes.
- Student record 0 contains a master password.
- Question record 0 contains exam metadata.
- Class names are parsed using fixed character positions.
- A completion marker file determines whether an exam was attempted.
- The application changes the process current working directory.
- Windows network shares are used for application data.
- A Windows mutex prevents multiple application instances.

Do not remove these behaviours simply because they appear unusual.
First determine why they exist and propose a migration strategy.

## Security

Never commit or expose:

- LL.txt
- network credentials
- real student passwords
- personally identifiable student data

LL.txt must remain excluded from Git.