---
name: power-automate-pro
description: >
  Expert Power Automate Cloud (PAC) and Desktop (PAD) developer skill. Use for ANY task
  involving Power Automate, cloud flows, desktop flows, RPA, connectors, WFL expressions,
  SharePoint, Excel Online, Outlook, Teams, UI automation, web scraping, SQL in PAD,
  attended/unattended bots, error handling, scope, apply to each, do until, variables,
  compose, parse JSON, OData filters, HTTP connector, retry policy, run desktop flow,
  Python/PowerShell scripting in PAD, or any PA expression debugging. Covers: WFL syntax
  and full function reference; PAC connectors (SharePoint, Excel Online Business, Outlook
  V2/V3, Teams, HTTP); Try/Catch/Finally patterns; PAD percent notation; PAD regex via
  action toggles (MatchesRegex does not exist); PAD UI automation with element-exists checks;
  PAD Excel/SQL/file operations; PAD scripting; guardrails for both engines.
  Copilot Studio integration with Power Automate (trigger flows from agents, return values, async patterns).
risk: low
source: custom
date_added: "2026-03-10"
---

# Power Automate Pro -- Developer Skill

## Core Mandate
Produce **complete, production-ready, immediately runnable** solutions.
- No placeholders. No "fill this in later."
- Always include error handling appropriate to context.
- PAC: validated WFL syntax only. PAD: %VarName% notation only (unless Power Fx explicitly enabled).
- When uncertain about an action name, parameter, or expression -- use the Microsoft Learn MCP tools first.

---

## CRITICAL GUARDRAILS

### PAC Guardrails
1. **WFL only -- never Power Fx.** PAC uses Workflow Definition Language. Wrong function names from Power Fx, JavaScript, or C# are the number one source of broken expressions.
2. **Always use ? null-safe operator**: `triggerBody()?['field']` not `triggerBody()['field']`. Missing ? crashes when a field is absent.
3. **String literals use single quotes**: `equals(variables('x'), 'Active')` -- double quotes break WFL.
4. **body() vs outputs()**: `body('ActionName')` for response content; `outputs('ActionName')` only when you need headers or status code.
5. **Never fabricate connector parameters.** Use Microsoft Learn MCP tools when uncertain.
6. **Initialize variable at global scope only** -- not inside Conditions, Scopes, or Apply to each loops.
7. **Apply to each is sequential by default.** Variables inside concurrent loops return unpredictable results.
8. **Use current action versions**: "Send an email (V2)", "When a new email arrives (V3)", "Post message in a chat or channel" -- not deprecated V1s.
9. **Environment variables** are retrieved via `parameters('env_var_name')` -- not `variables()`.

### PAD Guardrails
1. **MatchesRegex() is invalid in PAD.** No inline regex expression functions exist. Regex is done via action toggles only (Parse text, Replace text, Split text).
2. **PAD regex engine is .NET.** All patterns must be valid .NET regex.
3. **All variables use %VarName% notation** inside fields and expressions.
4. **Power Fx in PAD is opt-in at flow creation.** Never assume enabled. Default = % notation.
5. **Reserved keywords cannot be variable names**: ACTION, AND, AS, BLOCK, CALL, CASE, DEFAULT, DISABLE, ELSE, END, ERROR, EXIT, FALSE, FOR, FOREACH, FROM, FUNCTION, GLOBAL, GOTO, IF, IMPORT, IN, INPUT, LABEL, LOOP, MAIN, MOD, NEXT, NO, NOT, ON, OR, OUTPUT, REPEAT, SET, STEP, SWITCH, THEN, THROW, TIMES, TO, TRUE, WAIT, WHILE, XOR, YES.
6. **UI automation requires element-exists checks + On Block Error.** Never interact without confirming element presence first.
7. **Mark sensitive variables** (passwords, credentials) as Sensitive -- masks values in run history.
8. **Subflows must be defined before they are called.** Subflow names are case-sensitive.

---

## Architecture: PAC vs PAD vs Both

```
Need automation?
  Triggered by event / schedule / button?              PAC Cloud Flow
  Legacy desktop UI, mainframe, thick client?         PAD Desktop Flow
  Web scraping without APIs?                          PAD Browser Automation
  SharePoint / M365 / Excel Online only, no UI?       PAC Standard connectors
  Cloud trigger + desktop action?                     PAC triggers PAD via
                                                       "Run a flow built with
                                                        Power Automate for desktop"
  Mixed: API data + UI interaction?                   PAC orchestrates PAD subflows
  Human approval required?                            PAC Approvals connector
  Structured business data?                           PAC + Dataverse connector
  Power Apps form submission?                         PAC with PA trigger + respond action
  Copilot Studio agent action?                        Cloud flow with Power Apps/Copilot trigger
```

**PAC to PAD integration notes:**
- Connection reference required (attended vs unattended)
- Pass inputs/outputs as JSON
- Unattended: machine registered + Power Automate Premium + unattended add-on
- Attended: runs on active user session -- cannot run on locked screen

---

# =====================================================
# SECTION 1: POWER AUTOMATE CLOUD (PAC)
# =====================================================

## Trigger Types and Body Schemas

| Trigger | Key body fields |
|---|---|
| SharePoint: When item created/modified | `triggerBody()?['ID']`, `triggerBody()?['Title']`, `triggerBody()?['{FieldInternalName}']` |
| Outlook: When a new email arrives (V3) | `triggerBody()?['from']`, `triggerBody()?['subject']`, `triggerBody()?['body']`, `triggerBody()?['attachments']` |
| Teams: When a message is posted | `triggerBody()?['messageText']`, `triggerBody()?['from']?['user']?['displayName']` |
| HTTP Request | `triggerBody()` = parsed JSON body; `triggerOutputs()?['headers']` for headers |
| Recurrence (scheduled) | No body; use `utcNow()` for current timestamp |
| Power Apps / Copilot | `triggerBody()?['text']` etc. (dynamic per fields defined in trigger) |
| Manual / Button | Defined inputs; `triggerBody()?['inputs']?['FieldName']` |

**HTTP Request trigger -- define schema for typed access:**
```
When a HTTP request is received
  Method: POST
  Request Body JSON Schema: [paste schema generated from sample]
→ Dynamic content becomes typed fields throughout the flow
```

---

## WFL Expressions (Quick Ref)

```
// Data references (always null-safe)
triggerBody()?['Field']                   -- trigger payload
body('Action_Name')?['property']          -- action response body
outputs('Action_Name')?['statusCode']     -- full output (status, headers)
variables('VarName')                      -- flow variable
items('Apply_to_each')?['field']          -- current loop item
parameters('env_var_name')               -- environment variable

// Most-used functions
concat('Hello ', variables('Name'))
toLower(triggerBody()?['Email'])
substring(variables('Text'), 0, 5)
formatDateTime(utcNow(), 'yyyy-MM-dd')
convertTimeZone(utcNow(), 'UTC', 'Eastern Standard Time')
coalesce(triggerBody()?['Field'], 'default value')
if(equals(variables('Status'), 'Active'), 'Yes', 'No')
string(variables('MyNumber'))
int(triggerBody()?['Count'])
length(body('Get_items')?['value'])
first(body('Get_items')?['value'])
```

---

## PAC Variables

- Initialize at global scope only; one action per variable
- Types: Integer, Float, Boolean, String, Array, Object

| Action | Purpose |
|---|---|
| Initialize variable | Declare + set starting value |
| Set variable | Overwrite with new value (same type) |
| Increment variable | Add to Integer / Float |
| Append to string variable | Concatenate to string |
| Append to array variable | Add item to array |

---

## PAC Control Flow

**Condition** -- True/False branches. Advanced mode supports full WFL.
**Apply to Each** -- iterates array. Default sequential; concurrency up to 50 (Settings).
**Do Until** -- set Count limit and Timeout; include Delay action inside loop.
**Switch** -- discrete value matching; cleaner than nested conditions.
**Scope** -- groups actions; primary tool for try/catch.
**Parallel Branch** -- simultaneous execution; B must not depend on A.

---

## PAC Error Handling

```
[Scope: Try]     -- all main actions here
[Scope: Catch]   -- run after: has failed + has timed out + has been skipped
  Filter array: result('Try') where status != 'Succeeded'
  Error: first(body('Filter_array'))?['error']?['message']
[Scope: Finally] -- run after: all 4 states; cleanup always runs
```

---

## PAC Connectors (Quick Ref)

| Connector | Common Actions |
|---|---|
| SharePoint | Get items, Get item, Create/Update/Delete item, Get file content, Send HTTP request to SP |
| Excel Online (Business) | List rows in table, Add/Update/Delete row, Run script |
| Office 365 Outlook | Send email (V2), Reply (V3), Get emails (V3), Create event (V3) |
| Microsoft Teams | Post message in chat or channel, Post Adaptive Card and wait |
| HTTP (Premium) | GET/POST/PUT/PATCH/DELETE with auth; always parse response |
| Approvals | Start and wait for an approval, Create an approval, Get approval |
| Dataverse | List rows, Get row, Create row, Update row, Relate rows |
| Power Apps / Copilot | Respond to a PowerApp or flow |

---

## PAC Approvals

```
Start and wait for an approval
  Approval type: Approve/Reject - First to respond
              OR Approve/Reject - Everyone must approve
              OR Custom Responses - First responder
              OR Custom Responses - All must respond
  Title:       @{variables('RequestTitle')}
  Assigned to: approver@domain.com (or dynamic)
  Details:     [HTML supported]
  Item link:   [URL to related item]
  Item link description: [text]

→ Produces: %Outcome% ('Approve' / 'Reject')
            %Responses% (array, each has: approverResponse, approver, comments, requestDate)
            %SelectedOption%

After action:
  Condition: equals(body('Start_and_wait_for_an_approval')?['outcome'], 'Approve')
    True → approved path
    False → rejected path
```

---

## PAC Environment Variables

Environment variables are configured in the solution and consumed at runtime.
```
// Reference in expressions:
parameters('env_var_name')

// Types: String, Number, Boolean, JSON, Dataverse data source, Secret
// Defined in: Solution → Environment variables → +New
// Cannot be modified at flow runtime -- set at deployment/environment level
// For secrets: store in Azure Key Vault, reference via Dataverse secret type
```

---

## PAC Dataverse Connector (Quick Ref)

| Action | Notes |
|---|---|
| List rows | OData filter, select columns, expand related; default 100 rows |
| Get a row by ID | Single record by GUID |
| Create a new row | All required fields; lookup fields use GUID |
| Update a row | By ID; only changed fields needed |
| Delete a row | By ID |
| Perform a bound action | Custom Dataverse actions |
| Execute a changeset request | Transactional batch operations |
| Search rows (preview) | Relevance search across tables |

```
// OData filter for Dataverse List rows
_ownerid_value eq '@{variables('UserID')}'
statecode eq 0
createdon ge @{addDays(utcNow(), -30)}

// Expand related table
$expand=LookupTableName($select=columnname)
```

---

## PAC Power Apps Integration

```
// Trigger: Power Apps calls this flow
Trigger: PowerApps (in When a PowerApp calls a flow)
  → Each input defined becomes triggerBody()?['inputname']

// End: return data back to Power Apps
Respond to a PowerApp or flow
  Output fields: define name + type + expression
  → These become available in Power Apps as FlowName.Run().outputname
```

---

## PAC Output Standards
1. Overview: trigger type + flow purpose
2. Prerequisites: connections, permissions, licenses
3. Numbered steps: action name + connector + key config + expressions
4. Key expressions in code blocks
5. Error handling scope
6. Testing instructions

---

# =====================================================
# SECTION 2: POWER AUTOMATE DESKTOP (PAD)
# =====================================================

## PAD Action Categories

| Category | Key Actions |
|---|---|
| Variables | Set variable, Increase variable, Truncate number, Generate random |
| Flow control | IF, LOOP, FOR EACH, SWITCH, EXIT LOOP, GOTO, LABEL |
| Subflows | CALL subflow, Run subflow, define with FUNCTION |
| Error handling | ON BLOCK ERROR, Get last error, THROW, Log message |
| UI Automation (Web) | Launch browser, Navigate, Click, Fill text, Extract data |
| UI Automation (Desktop) | Click UI element, Fill text in window, Get UI element details |
| Excel | Launch Excel, Read/Write worksheet, Close Excel |
| Database / SQL | Open SQL connection, Execute SQL, Close connection |
| File / Folder | Get files, Copy/Move/Delete file, Read/Write text |
| System | Get environment variable, Set Windows environment variable |
| Process | Run application, Get process, Kill process, Wait for process |
| Clipboard | Get/Set clipboard text |
| Mouse/Keyboard | Send keys, Move mouse, Click, Mouse button action |
| OCR | Extract text with OCR (Tesseract / Windows OCR) |
| Scripting | Run PowerShell, Run VBScript, Run Python, Run JavaScript |
| Email (SMTP/IMAP) | Send email, Retrieve email (IMAP/POP3/Exchange) |
| Outlook (desktop) | Launch Outlook, Send, Get messages, Process messages |
| PDF | Extract text from PDF, Extract pages, Merge PDFs |
| Compression | ZIP files, Unzip archive |
| Cryptography | Encrypt/Decrypt text, Hash text |
| FTP / SFTP | Open FTP connection, Upload/Download, List directory |
| Dialogs | Display message, Input dialog, File select dialog |
| Date/Time | Get current date and time, Add to datetime, Format datetime |
| Text | Append to text, Change text case, Trim text, Convert to number |
| Lists | Create list, Add to list, Remove from list, Sort list |
| Data Tables | Create/Read/Write/Filter data table, Find or replace |

---

## PAD Expression System

```
%MyVariable%                      -- variable reference
%MyList[0]%                       -- list item (0-based)
%MyObject.PropertyName%           -- custom object property
%'Hello ' + UserName%             -- string concat
%Counter + 1%                     -- arithmetic
%Counter = 10%                    -- comparison (returns True/False)
%Contains(Text, 'INV', False)%    -- built-in string check
%IsEmpty(UserInput)%              -- blank check
%StartsWith(FileName, 'INV', True)%
%NOT(Counter = 0)%
%Index = 1 OR Index = 2%
%Index = 4 AND Status = 'Active'%
```

---

## PAD Control Flow

```
IF %Counter > 0% THEN
  ...
ELSE
  ...
END

FOR EACH CurrentItem IN %MyList%
  ...
END

LOOP LoopIndex FROM 1 TO %TotalCount% STEP 1
  ...
END

SWITCH %Status%
  CASE 'Active'
    ...
  DEFAULT
    ...
END
```

---

## PAD Error Handling

```
ON BLOCK ERROR
  GOTO ErrorHandler
END

... risky actions ...

GOTO Done

LABEL ErrorHandler
  Get last error
    → Produces: %LastError%
  THROW 'Descriptive context: ' + %LastError%

LABEL Done
```

---

## PAD Subflows (Quick Ref)

```
// Define subflow (in Subflows tab or at bottom of Main)
FUNCTION ProcessRecord (INOUT RecordData, IN RecordID, OUT ResultStatus)
  ... logic ...
  SET ResultStatus TO 'Complete'
END FUNCTION

// Call subflow
CALL ProcessRecord (RecordData, %CurrentID%, ResultStatus)

// Input parameters: IN (read-only), INOUT (modified in-place), OUT (returned value)
```

---

## PAD UI Automation
Mandatory pattern for all UI interaction:

```
IF UI element exists in window (MyElement, MyWindow) THEN
  Wait for UI element to appear
    UI element: MyElement
    Timeout: 30
  Click UI element in window
    UI element: MyElement
ELSE
  THROW 'Expected element not found: [description]'
END

ON BLOCK ERROR
  GOTO ErrorHandler
END
```

---

## PAD Excel / Database / File Operations

- **Excel**: Launch → Read from worksheet → Loop %ExcelData% → Write → Close with save
- **SQL**: Open SQL connection → Execute SQL → Use %QueryResult% DataTable → Close
- **File**: Get files in folder (filter *.ext) → For Each → Get file path parts → Process

---

## PAD Scripting (Quick Ref)

```
Run PowerShell script
  Script: [full PowerShell code]
  → Produces: %ScriptOutput%, %ScriptError%, %ScriptExitCode%

Run Python script
  Script: [Python code]
  → Produces: %PythonScriptOutput%

Run VBScript
  Script: [VBScript code]
  → Produces: %VBScriptOutput%
```

---

## PAD Output Standards
1. Overview + Prerequisites (app versions, credentials, dependencies)
2. Full script block -- complete, copy-paste ready, no gaps
3. Variable declarations at top, labeled with purpose
4. Inline comments on non-obvious logic
5. Error handler at bottom with descriptive THROW messages

---

# =====================================================
# SECTION 3: CROSS-PLATFORM
# =====================================================

## Licensing
| Feature | License Required |
|---|---|
| Cloud flows -- standard connectors | Microsoft 365 or Power Automate per-user |
| Premium connectors (HTTP, SQL, Dataverse, etc.) | Power Automate Premium |
| Attended desktop flows | Power Automate Premium |
| Unattended desktop flows | Power Automate Premium + unattended add-on |
| Approvals | Power Automate per-user or Microsoft 365 (basic); Premium for advanced |
| AI Builder actions | AI Builder credits |
| Environment variables | Any (part of solutions) |

## When to Fetch Live Microsoft Learn Docs
Use the `microsoft_docs_search` and `microsoft_docs_fetch` MCP tools (available in this environment) for:
- Action name, connector parameter, or action version is uncertain
- User reports a runtime error suggesting a schema or connector issue
- Topic involves PAD version-specific behavior
- Licensing questions arise
- Dataverse table schema or API action signatures needed

Usage:
- `microsoft_docs_search` — quick lookup, returns top results with excerpts
- `microsoft_docs_fetch` — full page content from a specific Microsoft Learn URL

Key reference URLs (for use with `microsoft_docs_fetch`):
- PAD Actions Reference: https://learn.microsoft.com/power-automate/desktop-flows/actions-reference
- PAD Variable Notation: https://learn.microsoft.com/power-automate/desktop-flows/variable-manipulation
- WFL Functions Reference: https://learn.microsoft.com/azure/logic-apps/workflow-definition-language-functions-reference
- PAC Connectors Reference: https://learn.microsoft.com/connectors/connector-reference/connector-reference-powerautomate-connectors
- PAC Error Handling: https://learn.microsoft.com/power-automate/guidance/coding-guidelines/error-handling
- PAC Approvals: https://learn.microsoft.com/power-automate/modern-approvals
- Dataverse Connector: https://learn.microsoft.com/connectors/commondataserviceforapps
- PAD .NET Regex: https://learn.microsoft.com/dotnet/standard/base-types/regular-expression-language-quick-reference

## Default Assumptions (state when applied)
- PAC: WFL expression engine unless user specifies otherwise
- PAD: % notation unless Power Fx explicitly enabled at flow creation
- Environment: production-grade -- error handling always included
- SharePoint: SharePoint Online unless stated
- Excel: Excel Online (Business) connector unless stated
- SQL: SQL Server with Windows or SQL auth
- Email: Office 365 / Exchange unless stated otherwise

---

# =====================================================
# SECTION 4: COPILOT STUDIO + POWER AUTOMATE
# =====================================================

## Integration Patterns
- Copilot Studio agents can trigger cloud flows via the "Run a Power Automate cloud flow" action node
- Cloud flows return output variables back to the agent as topic variables
- Use cloud flows for: external API calls, SharePoint/Excel operations, data lookups, email/Teams notifications
- Keep flows focused on single operations; compose complex logic from multiple flow calls

## Key Patterns
| Pattern | How |
|---|---|
| Agent calls flow | Action node → "Run a cloud flow" → select flow → map inputs |
| Flow returns data | "Respond to Copilot" action (or "Return value(s) to Power Virtual Agents") |
| Pass context | Topic variables → flow input parameters (string, number, boolean, table) |
| Error surfacing | Flow scope Try/Catch → return error message string to agent |
| Unattended desktop from agent | Cloud flow with "Run a flow built with Power Automate for desktop" (unattended) |

## Guardrails
- Flows called from Copilot Studio must use the **Power Apps / Copilot** trigger type
- Output variable names must match exactly (case-sensitive) between flow and agent topic
- Long-running flows will time out the agent turn — keep under 30s or use async pattern
- Test flows independently in Power Automate before connecting to Copilot Studio
