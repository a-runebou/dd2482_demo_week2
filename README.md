**The pull request must both contain a README.md and have description following the template below. This README.md must be the only file affected by the PR, and its contents must match the PR description exactly. The pull request must be created 3 business days before the actual delivery.**

**The README.md file must be located in the directory**:

`contributions/<category>/[<week>/]<kth-id-1>-<kth-id-2>/README.md`

# Assignment Proposal

## Title

Beyond Code Coverage: Evaluating and Improving Test Suite Quality

## Names and KTH ID

  - Alexander Runebou (alerun@kth.se)
  - Student name 2 (student321@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

Our demo investigates why conventional code coverage is not always sufficient for evaluating the quality of a test suite. We will construct a small application with tests that achieve high or complete statement coverage while still failing to detect meaningful faults.

We will then introduce mutation testing in the workflow, where small artificial faults are automatically introduced into the program and the existing test suite is evaluated based on whether it detects them. Surviving mutations will expose weaknesses in the tests.

We can then improve the test suite using techniques such as boundary-value testing and property-based testing, and rerun the mutation tests to demonstrate how these approaches can make tests detect faults without necessarily changing the code coverage. We would also mention the downsides of adding mutation testing, such as the added time for running the tests, and how to balance this.

The workflow will be integrated into a CI pipeline so that coverage, mutation testing, and the improved tests act as automated validation mechanisms. During the live demo, we will change the workflow to use mutation testing and modify the tests.


**Relevance**

This demo is directly relevant to the topics of testing and verification and continuous integration. Automated tests are a central validation mechanism in CI pipelines, but commonly used metrics such as code coverage only measure if the code was executed and do not necessarily indicate whether the tests can detect incorrect behaviour.

Mutation testing can catch these errors and therefore provides a stronger form of automated verification. Combining mutation testing with boundary-value and property-based testing demonstrates how different testing techniques complement each other. 


