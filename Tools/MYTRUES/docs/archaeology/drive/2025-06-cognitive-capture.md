<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source: Google Drive
Drive file id: 15M3gRt89spmgsT9S6QCzXPLhGv9fGCtc
Source URL: https://drive.google.com/file/d/15M3gRt89spmgsT9S6QCzXPLhGv9fGCtc/view?usp=drivesdk
Original title: cognitive_capture.md
Reason preserved: 2025-06 EDTAgent dual capture specification
-->

# EDTAgent: Cognitive Capture Implementation

## 🤖 EDTAgent Definition

EDTAgent é a **implementação operacional** da filosofia EDT. É um agente cognitivo que:

1. **Captura cognições** em tempo real (OMGDiary)
2. **Cristaliza conhecimento** validado (MyTrues) 
3. **Mantém rastreabilidade** entre episódios e verdades
4. **Evolui continuamente** através de feedback loops

## 🔄 Dual Capture Process

### Sequential Capture (OMGDiary)
```yaml
omg_entry:
  uuid: temporal_unique_identifier
  timestamp: cognitive_moment
  context:
    project: "{{projeto}}"
    domain: "{{domínio}}"
    session: current_session_id
  cognitive_state:
    emotional_context: [curiosidade, frustração, eureka, ...]
    focus_level: [scattered, focused, flow, ...]
    energy_level: [low, medium, high, peak]
  content:
    trigger: what_sparked_cognition
    process: thinking_pathway
    conclusion: cognitive_result
    omg_factor: impact_significance_0_10
  connections:
    related_trues: [TRUE-IDs que foram consultadas]
    generated_trues: [TRUE-IDs criadas a partir desta cognição]
    previous_omg: [OMG-IDs relacionados]
```

### Neural Capture (MyTrues)
```yaml
true_entry:
  uuid: TRUE-{DOMAIN}-{SEQ}
  version: semantic_versioning
  type: [abstract, concrete, specialized, experiential]
  essence: immutable_core_concept
  context:
    variables: ["{{var1}}", "{{var2}}"]
    application_scope: domain_boundaries
    confidence_level: validation_strength_0_10
  manifestation:
    current_implementation: how_it_exists_today
    alternatives: other_possible_approaches
    constraints: limitations_and_boundaries
  synapses:
    vertical:
      parent: TRUE-ID-of-more-abstract-concept
      children: [TRUE-IDs-of-specializations]
    horizontal:
      alternatives: [TRUE-IDs-of-equivalent-solutions]
      variants: [TRUE-IDs-of-similar-approaches]
    contextual:
      applications: [TRUE-IDs-in-specific-contexts]
  provenance:
    ccc_origin: OMG-ID-that-generated-this-TRUE
    validation_path: how_this_was_confirmed
    last_review: when_this_was_last_validated
```

## 🎯 Capture Triggers

### Automatic Triggers
- **Decision Points**: When choosing between alternatives
- **Problem Solving**: When finding solutions
- **Pattern Recognition**: When noticing repeated situations
- **Error Discovery**: When finding mistakes or better approaches

### Manual Triggers  
- **Eureka Moments**: Sudden insights
- **Learning Events**: New knowledge acquisition
- **Reflection Periods**: Deliberate knowledge review
- **Knowledge Transfer**: Preparing information for others

## 🧠 Cognitive Processing Workflow

### 1. Initial Capture
```mermaid
Cognitive Event → OMGDiary Entry → Temporary Storage
```

### 2. Processing Phase
```mermaid
OMGDiary → Pattern Analysis → TRUE Candidate → Validation
```

### 3. Crystallization
```mermaid
Validated Insight → TRUE Creation → Synaptic Integration → Neural Update
```

### 4. Feedback Loop
```mermaid
Neural State → Inform Future Decisions → Generate New Cognitions
```

## 🔍 Pattern Recognition Engine

### Automatic Pattern Detection
- **Repeated Decisions**: Same choices in similar contexts
- **Evolution Patterns**: How solutions improve over time
- **Context Patterns**: Which approaches work in which situations
- **Failure Patterns**: What consistently doesn't work

### TRUE Generation Criteria
1. **Validation**: Confirmed through multiple applications
2. **Generalization**: Applicable beyond original context
3. **Significance**: Impact level justifies documentation
4. **Uniqueness**: Not already captured in existing TRUEs

## 🌐 Variable Resolution System

### Context Substitution
```yaml
template: "Use {{tool}} for {{purpose}} in {{context}}"
resolution_rules:
  - "{{tool}}": lookup in TOOL domain TRUEs
  - "{{purpose}}": infer from current problem space
  - "{{context}}": current project/environment variables
result: "Use ASDF for version management in Node.js projects"
```

### Inheritance Resolution
```yaml
specialized_true:
  inherits_from: parent_true_id
  overrides:
    - manifestation: project_specific_implementation
    - constraints: additional_limitations
  preserves:
    - essence: unchanged_core_concept
    - validation_rules: same_confirmation_criteria
```

## 📊 Quality Assurance

### Consistency Checks
- **Synaptic Integrity**: All references point to valid TRUEs
- **Version Coherence**: No contradictory versions
- **Temporal Logic**: Cause-effect relationships make sense
- **Context Validity**: Variables resolve to valid values

### Validation Workflows
1. **Self-Validation**: Agent checks its own captures
2. **Cross-Validation**: Compare with existing knowledge
3. **Human Review**: Strategic validation by human operators
4. **Temporal Validation**: Confirm accuracy over time

## 🔄 Learning Mechanisms

### Reinforcement Learning
- **Success Patterns**: Strengthen successful TRUE applications
- **Failure Analysis**: Identify and correct unsuccessful patterns
- **Context Adaptation**: Adjust applications based on environment
- **Evolution Tracking**: Monitor how knowledge changes

### Meta-Learning
- **Capture Quality**: Learn what makes good cognitive captures
- **Pattern Recognition**: Improve ability to identify patterns
- **Validation Efficiency**: Optimize validation processes
- **Transfer Learning**: Better knowledge application across contexts

## 🎪 Implementation Interfaces

### For Humans
- **OMG Prompts**: Strategic questions to trigger capture
- **TRUE Templates**: Structured forms for knowledge entry
- **Review Dashboards**: Visual interfaces for validation
- **Search Interfaces**: Query both streams effectively

### For AIs
- **Capture APIs**: Programmatic cognitive capture
- **Pattern APIs**: Access to pattern recognition
- **Query APIs**: Structured knowledge retrieval
- **Update APIs**: Knowledge evolution mechanisms

## 🔮 Extension Points

### Custom Domains
- **Domain-Specific Templates**: Tailored capture for specific fields
- **Specialized Validation**: Custom rules for domain knowledge
- **Context Resolvers**: Domain-specific variable resolution
- **Pattern Libraries**: Pre-built patterns for common domains

### Integration Hooks
- **External Knowledge**: Connect to external knowledge bases
- **Tool Integration**: Link with development/work tools
- **Collaboration Systems**: Multi-agent knowledge sharing
- **Export Formats**: Knowledge portability mechanisms

---

*Bootstrap Temporal Note: This EDTAgent specification exists independently of any specific implementation and can be adapted to any cognitive capture system.*
