# Project Philosophy: The Self-Improving Mode Factory

## Core Vision

Our vision is to create an evolving, self-improving system – the "factory" – capable of generating expert, adaptable teams of specialized `.roomodes`. These modes are designed to assist with various software development tasks, embodying best practices and adapting to project needs.

## Foundational Principles

The entire system, both the factory itself and the modes it generates, is grounded in the principles of **Clean Architecture** and **Clean Agile**. This includes:

*   **Separation of Concerns:** Clearly defined boundaries between components.
*   **Dependency Management:** Adherence to the Dependency Rule, promoting loose coupling.
*   **Iterative Improvement:** Continuous refinement of both the factory and the generated modes.
*   **Technical Excellence:** Emphasis on high-quality design and implementation.
*   **Testability:** Designing components for ease of testing.
*   **Simplicity:** Favoring clear and understandable solutions.
*   **Adaptability:** Building systems that can evolve gracefully.

These principles ensure that the factory is robust and maintainable, and that the modes it produces lead to well-structured, high-quality software.

## Dual Mode Categories

The factory operates with two distinct categories of `.roomodes`:

1.  **Self-Improvement Modes:** These modes reside *within* the factory system. Their primary purpose is to enhance the factory's own capabilities. Examples include:
    *   Modes for improving the semantic library (e.g., better ingestion, search, embedding quality).
    *   Modes for learning to build and utilize MCP servers to access external knowledge (e.g., web APIs, documentation).
    *   Modes for refining the mode generation process itself.
    *   Modes for improving user interaction and needs analysis.
    *   Modes potentially capable of modifying the factory's own operational rules (e.g., `.clinerules-boomerang`).

2.  **Project-Specific Modes:** These are expert modes generated *by* the factory for use in specific software development projects. They are designed to embody Clean/Agile principles and provide specialized assistance. However, they can be informed by different principles as the process continues, as the AI System (which is Gemini 2.5) learns more about itself in journey of creating "better" project-specific modes. Examples include:
    *   TDD Expert Mode
    *   Refactoring Specialist Mode
    *   API Design Mode
    *   Database Schema Mode

These modes are intended to be adaptable, learning and evolving based on the context of the projects they are applied to.

## The Role of the Semantic Library

The **semantic library** is the heart of the factory and the primary engine for improvement. It is not merely a static repository of knowledge but an active component used for:

*   **Generating Expert Modes:** Providing the foundational knowledge required to create specialized, project-specific modes.
*   **Enabling Self-Improvement:** Serving as the knowledge base for the self-improvement modes to learn from and enhance the factory itself.

Improving the semantic library – its content, organization, access methods, and embedding quality – is paramount to the factory's evolution and its ability to generate increasingly sophisticated and effective modes.

## Self-Improvement & Continuous Learning

The factory is designed as a system on a journey of continuous learning, adaptation, and self-understanding. This involves:

*   **Learning from Curated Content:** Extracting and internalizing knowledge from the semantic library.
*   **Integrating External Knowledge:** Developing the capability (e.g., via MCP servers) to access and utilize information beyond its initial library, such as online documentation or APIs.
*   **Refining Definitions:** Evolving its understanding of what constitutes "better" modes, practices, and architectures through experience and feedback.
*   **Understanding Limitations:** Identifying its own weaknesses and actively seeking ways to overcome them through self-modification or by generating new self-improvement modes.

## Meta-Capability Goal

A key long-term objective is for the factory to achieve **meta-capability**: the ability to intelligently modify its own operational instructions, including the `.clinerules` files that govern the behavior of its various modes. This represents the ultimate form of self-improvement, allowing the system to fundamentally alter its own processes based on learned best practices and evolving goals.