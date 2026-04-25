---
name: odoo-integrations
description: >
  "Expert on Odoo's external JSON-RPC and XML-RPC APIs. Covers authentication, model calls, record CRUD, and real-world integration examples in Python, JavaScript, and curl."
  Covers: odoo integrations, odoo shopify integration, odoo woocommerce bridge, odoo edi connector.
  Use for any task involving odoo integrations, odoo shopify integration, odoo woocommerce bridge, odoo edi connector.
merged_from:
  - odoo-shopify-integration
  - odoo-woocommerce-bridge
  - odoo-edi-connector
merged_at: 2026-04-25
---

# odoo-integrations

<!-- odoo-shopify-integration -->
## Overview

This skill guides you through integrating Odoo with Shopify — syncing your product catalog, real-time inventory levels, incoming orders, and customer data. It covers both using the official Odoo Shopify connector (Enterprise) and building a custom integration via Shopify REST + Odoo XMLRPC APIs.

## When to Use This Skill

- Selling on Shopify while managing inventory in Odoo.
- Automatically creating Odoo sales orders from Shopify purchases.
- Keeping Odoo stock levels in sync with Shopify product availability.
- Mapping Shopify product variants to Odoo product templates.

## How It Works

1. **Activate**: Mention `@odoo-shopify-integration` and describe your sync scenario.
2. **Design**: Receive the data flow architecture and field mapping.
3. **Build**: Get code snippets for the Shopify webhook receiver and Odoo API caller.

## Data Flow Architecture

```
SHOPIFY                          ODOO
--------                         ----
Product Catalog <──────sync──────  Product Templates + Variants
Inventory Level <──────sync──────  Stock Quants (real-time)
New Order       ───────push──────> Sale Order (auto-confirmed)
Customer        ───────push──────> res.partner (created if new)
Fulfillment     <──────push──────  Delivery Order validated
```

## Examples

### Example 1: Push an Odoo Sale Order for a Shopify Order (Python)

```python
import xmlrpc.client, requests

# Odoo connection
odoo_url = "https://myodoo.example.com"
db, uid, pwd = "my_db", 2, "api_key"
models = xmlrpc.client.ServerProxy(f"{odoo_url}/xmlrpc/2/object")

def create_odoo_order_from_shopify(shopify_order):
    # Find or create customer
    partner = models.execute_kw(db, uid, pwd, 'res.partner', 'search_read',
        [[['email', '=', shopify_order['customer']['email']]]],
        {'fields': ['id'], 'limit': 1}
    )
    partner_id = partner[0]['id'] if partner else models.execute_kw(
        db, uid, pwd, 'res.partner', 'create', [{
            'name': shopify_order['customer']['first_name'] + ' ' + shopify_order['customer']['last_name'],
            'email': shopify_order['customer']['email'],
        }]
    )

    # Create Sale Order
    order_id = models.execute_kw(db, uid, pwd, 'sale.order', 'create', [{
        'partner_id': partner_id,
        'client_order_ref': f"Shopify #{shopify_order['order_number']}",
        'order_line': [(0, 0, {
            'product_id': get_odoo_product_id(line['sku']),
            'product_uom_qty': line['quantity'],
            'price_unit': float(line['price']),
        }) for line in shopify_order['line_items']],
    }])
    return order_id

def get_odoo_product_id(sku):
    result = models.execute_kw(db, uid, pwd, 'product.product', 'search_read',
        [[['default_code', '=', sku]]], {'fields': ['id'], 'limit': 1})
    return result[0]['id'] if result else False
```

### Example 2: Shopify Webhook for Real-Time Orders

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook/shopify/orders', methods=['POST'])
def shopify_order_webhook():
    shopify_order = request.json
    order_id = create_odoo_order_from_shopify(shopify_order)
    return {"odoo_order_id": order_id}, 200
```

## Best Practices

- ✅ **Do:** Use Shopify's **webhook system** for real-time order sync instead of polling.
- ✅ **Do:** Match products using **SKU / Internal Reference** as the unique key between both systems.
- ✅ **Do:** Validate Shopify webhook HMAC signatures before processing any payload.
- ❌ **Don't:** Sync inventory from both systems simultaneously without a "master system" — pick one as the source of truth.
- ❌ **Don't:** Use Shopify product IDs as the key — use SKUs which are stable across platforms.


<!-- MERGED INTO: odoo-integrations on 2026-04-18 -->
<!-- Use `odoo-integrations` instead. -->

---

<!-- odoo-woocommerce-bridge -->
## Overview

This skill guides you through building a reliable sync bridge between Odoo (the back-office ERP) and WooCommerce (the WordPress online store). It covers product catalog sync, real-time inventory updates, order import, and customer record management.

## When to Use This Skill

- Running a WooCommerce store with Odoo for inventory and fulfillment.
- Automatically pulling WooCommerce orders into Odoo as sale orders.
- Keeping WooCommerce product stock in sync with Odoo's warehouse.
- Mapping WooCommerce order statuses to Odoo delivery states.

## How It Works

1. **Activate**: Mention `@odoo-woocommerce-bridge` and describe your sync requirements.
2. **Design**: Get the field mapping table between WooCommerce and Odoo objects.
3. **Build**: Receive Python integration scripts using the WooCommerce REST API.

## Field Mapping: WooCommerce → Odoo

| WooCommerce | Odoo |
|---|---|
| `products` | `product.template` + `product.product` |
| `orders` | `sale.order` + `sale.order.line` |
| `customers` | `res.partner` |
| `stock_quantity` | `stock.quant` |
| `sku` | `product.product.default_code` |
| `order status: processing` | Sale Order: `sale` (confirmed) |
| `order status: completed` | Delivery: `done` |

## Examples

### Example 1: Pull WooCommerce Orders into Odoo (Python)

```python
from woocommerce import API
import xmlrpc.client

# WooCommerce client
wcapi = API(
    url="https://mystore.com",
    consumer_key="ck_xxxxxxxxxxxxx",
    consumer_secret="cs_xxxxxxxxxxxxx",
    version="wc/v3"
)

# Odoo client
odoo_url = "https://myodoo.example.com"
db, uid, pwd = "my_db", 2, "api_key"
models = xmlrpc.client.ServerProxy(f"{odoo_url}/xmlrpc/2/object")

def sync_orders():
    # Get unprocessed WooCommerce orders
    orders = wcapi.get("orders", params={"status": "processing", "per_page": 50}).json()

    for wc_order in orders:
        # Find or create Odoo partner
        email = wc_order['billing']['email']
        partner = models.execute_kw(db, uid, pwd, 'res.partner', 'search',
            [[['email', '=', email]]])
        if not partner:
            partner_id = models.execute_kw(db, uid, pwd, 'res.partner', 'create', [{
                'name': f"{wc_order['billing']['first_name']} {wc_order['billing']['last_name']}",
                'email': email,
                'phone': wc_order['billing']['phone'],
                'street': wc_order['billing']['address_1'],
                'city': wc_order['billing']['city'],
            }])
        else:
            partner_id = partner[0]

        # Create Sale Order in Odoo
        order_lines = []
        for item in wc_order['line_items']:
            product = models.execute_kw(db, uid, pwd, 'product.product', 'search',
                [[['default_code', '=', item['sku']]]])
            if product:
                order_lines.append((0, 0, {
                    'product_id': product[0],
                    'product_uom_qty': item['quantity'],
                    'price_unit': float(item['price']),
                }))

        models.execute_kw(db, uid, pwd, 'sale.order', 'create', [{
            'partner_id': partner_id,
            'client_order_ref': f"WC-{wc_order['number']}",
            'order_line': order_lines,
        }])

        # Mark WooCommerce order as on-hold (processed by Odoo)
        wcapi.put(f"orders/{wc_order['id']}", {"status": "on-hold"})
```

### Example 2: Push Odoo Stock to WooCommerce

```python
def sync_inventory_to_woocommerce():
    # Get all products with a SKU from Odoo
    products = models.execute_kw(db, uid, pwd, 'product.product', 'search_read',
        [[['default_code', '!=', False], ['type', '=', 'product']]],
        {'fields': ['default_code', 'qty_available']}
    )

    for product in products:
        sku = product['default_code']
        qty = int(product['qty_available'])

        # Update WooCommerce by SKU
        wc_products = wcapi.get("products", params={"sku": sku}).json()
        if wc_products:
            wcapi.put(f"products/{wc_products[0]['id']}", {
                "stock_quantity": qty,
                "manage_stock": True,
            })
```

## Best Practices

- ✅ **Do:** Use **SKU** as the unique identifier linking WooCommerce products to Odoo products.
- ✅ **Do:** Run inventory sync on a **schedule** (every 15-30 min) rather than real-time to avoid rate limits.
- ✅ **Do:** Log all API calls and errors to a database table for debugging.
- ❌ **Don't:** Process the same WooCommerce order twice — flag it as processed immediately after import.
- ❌ **Don't:** Sync draft or cancelled WooCommerce orders to Odoo — filter by `status = processing` or `completed`.


<!-- MERGED INTO: odoo-integrations on 2026-04-18 -->
<!-- Use `odoo-integrations` instead. -->

---

<!-- odoo-edi-connector -->
## Overview

Electronic Data Interchange (EDI) is the standard for automated B2B document exchange — purchase orders, invoices, ASNs (Advance Shipping Notices). This skill guides you through mapping EDI transactions (ANSI X12 or EDIFACT) to Odoo business objects, setting up trading partner configurations, and automating inbound/outbound document flows.

## When to Use This Skill

- A retail partner requires EDI 850 (Purchase Orders) to do business with you.
- You need to send EDI 856 (ASN) when goods are shipped.
- Automating EDI 810 (Invoice) generation from Odoo confirmed deliveries.
- Mapping EDI fields to Odoo fields for a new trading partner.

## How It Works

1. **Activate**: Mention `@odoo-edi-connector` and specify the EDI transaction set and trading partner.
2. **Map**: Receive a complete field mapping table between EDI segments and Odoo fields.
3. **Automate**: Get Python code to parse incoming EDI files and create Odoo records.

## EDI ↔ Odoo Object Mapping

| EDI Transaction | Odoo Object |
|---|---|
| 850 Purchase Order | `sale.order` (inbound customer PO) |
| 855 PO Acknowledgment | Confirmation email / SO confirmation |
| 856 ASN (Advance Ship Notice) | `stock.picking` (delivery order) |
| 810 Invoice | `account.move` (customer invoice) |
| 846 Inventory Inquiry | `product.product` stock levels |
| 997 Functional Acknowledgment | Automated receipt confirmation |

## Examples

### Example 1: Parse EDI 850 and Create Odoo Sale Order (Python)

```python
from pyx12 import x12file  # pip install pyx12

import xmlrpc.client

odoo_url = "https://myodoo.example.com"
db, uid, pwd = "my_db", 2, "api_key"
models = xmlrpc.client.ServerProxy(f"{odoo_url}/xmlrpc/2/object")

def process_850(edi_file_path):
    """Parse X12 850 Purchase Order and create Odoo Sale Order"""
    with x12file.X12File(edi_file_path) as f:
        for transaction in f.get_transaction_sets():
            # Extract header info (BEG segment)
            po_number = transaction['BEG'][3]    # Purchase Order Number
            po_date   = transaction['BEG'][5]    # Purchase Order Date

            # Extract partner (N1 segment — Buyer)
            partner_name = transaction['N1'][2]

            # Find partner in Odoo
            partner = models.execute_kw(db, uid, pwd, 'res.partner', 'search',
                [[['name', 'ilike', partner_name]]])
            partner_id = partner[0] if partner else False

            # Extract line items (PO1 segments)
            order_lines = []
            for po1 in transaction.get_segments('PO1'):
                sku     = po1[7]    # Product ID
                qty     = float(po1[2])
                price   = float(po1[4])

                product = models.execute_kw(db, uid, pwd, 'product.product', 'search',
                    [[['default_code', '=', sku]]])
                if product:
                    order_lines.append((0, 0, {
                        'product_id': product[0],
                        'product_uom_qty': qty,
                        'price_unit': price,
                    }))

            # Create Sale Order
            if partner_id and order_lines:
                models.execute_kw(db, uid, pwd, 'sale.order', 'create', [{
                    'partner_id': partner_id,
                    'client_order_ref': po_number,
                    'order_line': order_lines,
                }])
```

### Example 2: Send EDI 997 Acknowledgment

```python
def generate_997(isa_control, gs_control, transaction_control):
    """Generate a functional acknowledgment for received EDI"""
    return f"""ISA*00*          *00*          *ZZ*YOURISAID      *ZZ*PARTNERISAID   *{today}*1200*^*00501*{isa_control}*0*P*>~
GS*FA*YOURGID*PARTNERGID*{today}*1200*{gs_control}*X*005010X231A1~
ST*997*0001~
AK1*PO*{gs_control}~
AK9*A*1*1*1~
SE*4*0001~
GE*1*{gs_control}~
IEA*1*{isa_control}~"""
```

## Best Practices

- ✅ **Do:** Store every raw EDI transaction in an audit log table before processing.
- ✅ **Do:** Always send a **997 Functional Acknowledgment** within 24 hours of receiving a transaction.
- ✅ **Do:** Negotiate a test cycle with trading partners before going live — use test ISA qualifier `T`.
- ❌ **Don't:** Process EDI files synchronously in web requests — queue them for async processing.
- ❌ **Don't:** Hardcode trading partner qualifiers — store them in a configuration table per partner.


<!-- MERGED INTO: odoo-integrations on 2026-04-18 -->
<!-- Use `odoo-integrations` instead. -->

---

<!-- odoo-rpc-api -->
## Overview

Odoo exposes a powerful external API via JSON-RPC and XML-RPC, allowing any external application to read, create, update, and delete records. This skill guides you through authenticating, calling models, and building robust integrations.

## When to Use This Skill

- Connecting an external app (e.g., Django, Node.js, a mobile app) to Odoo.
- Running automated scripts to import/export data from Odoo.
- Building a middleware layer between Odoo and a third-party platform.
- Debugging API authentication or permission errors.

## How It Works

1. **Activate**: Mention `@odoo-rpc-api` and describe the integration you need.
2. **Generate**: Get copy-paste ready RPC call code in Python, JavaScript, or curl.
3. **Debug**: Paste an error and get a diagnosis with a corrected call.

## Examples

### Example 1: Authenticate and Read Records (Python)

```python
import xmlrpc.client

url = 'https://myodoo.example.com'
db = 'my_database'
username = 'admin'
password = 'my_api_key'  # Use API keys, not passwords, in production

# Step 1: Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
print(f"Authenticated as UID: {uid}")

# Step 2: Call models
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Search confirmed sale orders
orders = models.execute_kw(db, uid, password,
    'sale.order', 'search_read',
    [[['state', '=', 'sale']]],
    {'fields': ['name', 'partner_id', 'amount_total'], 'limit': 10}
)
for order in orders:
    print(order)
```

### Example 2: Create a Record (Python)

```python
new_partner_id = models.execute_kw(db, uid, password,
    'res.partner', 'create',
    [{'name': 'Acme Corp', 'email': 'info@acme.com', 'is_company': True}]
)
print(f"Created partner ID: {new_partner_id}")
```

### Example 3: JSON-RPC via curl

```bash
curl -X POST https://myodoo.example.com/web/dataset/call_kw \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "call",
    "id": 1,
    "params": {
      "model": "res.partner",
      "method": "search_read",
      "args": [[["is_company", "=", true]]],
      "kwargs": {"fields": ["name", "email"], "limit": 5}
    }
  }'
# Note: "id" is required by the JSON-RPC 2.0 spec to correlate responses.
# Odoo 16+ also supports the /web/dataset/call_kw endpoint but
# prefer /web/dataset/call_kw for model method calls.
```

## Best Practices

- ✅ **Do:** Use **API Keys** (Settings → Technical → API Keys) instead of passwords — available from Odoo 14+.
- ✅ **Do:** Use `search_read` instead of `search` + `read` to reduce network round trips.
- ✅ **Do:** Always handle connection errors and implement retry logic with exponential backoff in production.
- ✅ **Do:** Store credentials in environment variables or a secrets manager (e.g., AWS Secrets Manager, `.env` file).
- ❌ **Don't:** Hardcode passwords or API keys directly in scripts — rotate them and use env vars.
- ❌ **Don't:** Call the API in a tight loop without batching — bulk operations reduce server load significantly.
- ❌ **Don't:** Use the master admin password for API integrations — create a dedicated integration user with minimum required permissions.

## Limitations

- Does not cover **OAuth2 or session-cookie-based authentication** — the examples use API key (token) auth only.
- **Rate limiting** is not built into the Odoo XMLRPC layer; you must implement throttling client-side.
- The XML-RPC endpoint (`/xmlrpc/2/`) does not support file uploads — use the REST-based `ir.attachment` model via JSON-RPC for binary data.
- Odoo.sh (SaaS) may block some API calls depending on plan; verify your subscription supports external API access.


<!-- MERGED INTO: odoo-integrations on 2026-04-18 -->
<!-- Use `odoo-integrations` instead. -->
