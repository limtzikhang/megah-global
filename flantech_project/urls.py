from django.urls import path
from . import views

urlpatterns = [
    # Left Pane Link 1: Identity & Authentication
    path('', views.login_user, name='login_user'),
    path('signup/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('account/', views.account_detail, name='account_detail'),
    
    # Left Pane Link 2 & 3: Content Marketing Channels
    path('video/', views.product_video, name='product_video'),
    path('info/', views.product_info, name='product_info'),
    
    # Left Pane Link 4: Dynamic E-Commerce Cart Volume Controller
    path('cart/', views.cart_view, name='cart_view'),
    
    # Left Pane Link 5: Transaction Gateway Interface Routing Matrix
    path('payment-hub/', views.payment_gateway_hub, name='payment_gateway_hub'),
    path('payment-success/<int:quantity>/<str:is_signup>/', views.process_order_success, name='process_order_success'),
]
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flantech Mega H Operations Hub</title>
    <style>
        body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; height: 100vh; background: #f8f9fa; }
        .sidebar { width: 260px; background: #1e293b; color: white; display: flex; flex-direction: column; padding: 20px 0; box-shadow: 2px 0 5px rgba(0,0,0,0.1); }
        .sidebar h2 { text-align: center; font-size: 1.2rem; margin-bottom: 20px; color: #38bdf8; }
        .sidebar a { color: #cbd5e1; text-decoration: none; padding: 12px 24px; display: block; border-left: 4px solid transparent; font-size: 0.95rem; }
        .sidebar a:hover, .sidebar a.active { background: #334155; color: white; border-left-color: #38bdf8; }
        .main-content { flex: 1; padding: 40px; overflow-y: auto; }
        .card { background: white; border-radius: 8px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); max-width: 800px; }
        .btn { display: inline-block; background: #0284c7; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; font-weight: 500; }
        .btn:hover { background: #0369a1; }
        .alert { padding: 12px; background: #dcfce7; color: #166534; border-radius: 4px; margin-bottom: 20px; }
    </style>
</head>
<body>

    <!-- Unified Left Pane Navigational Hierarchy -->
    <div class="sidebar">
        <h2>Flantech Mega H</h2>
        <a href="{% url 'account_detail' %}">👤 1. Account Details / Sign In</a>
        <a href="{% url 'product_video' %}">📺 2. Product Video Assets</a>
        <a href="{% url 'product_info' %}">🔬 3. Product Scientific Info</a>
        <a href="{% url 'cart_view' %}">🛒 4. Configure Cart Quantity</a>
        <a href="{% url 'payment_gateway_hub' %}">💳 5. Malaysia Payment Matrix</a>
        {% if user.is_authenticated %}
            <a href="{% url 'logout_user' %}" style="margin-top:auto; color:#ef4444;">🚪 Sign Out</a>
        {% endif %}
    </div>

    <!-- Right Pane Data Sandbox Rendering Portal -->
    <div class="main-content">
        {% if messages %}
            {% for message in messages %}
                <div class="alert">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% block content %}{% endblock %}
    </div>

</body>
</html>
{% extends 'base.html' %}
{% block content %}
<div class="card">
    <h2>💳 5. Malaysia Integrated Payment Gateway Matrix</h2>
    <p>Complete checkout verification rules for your current order package allocation parameters.</p>
    
    <div style="background: #f1f5f9; padding: 16px; border-radius: 6px; margin-bottom: 24px;">
        <h3>Order Parameters Summary</h3>
        <p><strong>Quantity Set:</strong> {{ request.GET.quantity|default:"1" }} Bottle(s)</p>
        <p style="font-size: 1.1rem; color: #0f172a;">
            <strong>Target Transaction Pricing Context:</strong> 
            {% if request.GET.type == 'signup_6_pack' %}
                Downline Sign-up Tier (RM 198 / bottle)
            {% elif request.GET.quantity == '50' %}
                B2B Bulk Wholesale Tier (RM 148 / bottle)
            {% else %}
                Standard B2C Retail Tier (RM 248 / bottle)
            {% endif %}
        </p>
    </div>

    <form method="POST" action="{% url 'payment_gateway_hub' %}">
        {% csrf_token %}
        <input type="hidden" name="quantity" value="{{ request.GET.quantity|default:'1' }}">
        <input type="hidden" name="is_signup" value="{% if request.GET.type == 'signup_6_pack' %}True{% else %}False{% endif %}">

        <h3>Select Your Payment Channel:</h3>
        
        <div style="margin-bottom: 12px;">
            <label style="display: block; padding: 12px; border: 1px solid #cbd5e1; border-radius: 4px; cursor: pointer;">
                <input type="radio" name="gateway_choice" value="fpx" checked> 
                <strong>FPX Online Banking</strong> (Maybank2u, CIMB Clicks, Public Bank, RHB)
            </label>
        </div>

        <div style="margin-bottom: 12px;">
            <label style="display: block; padding: 12px; border: 1px solid #cbd5e1; border-radius: 4px; cursor: pointer;">
                <input type="radio" name="gateway_choice" value="razer"> 
                <strong>Razer Merchant Services / ToyyibPay</strong> (Cards & E-Wallets like TnG, Boost)
            </label>
        </div>

        <div style="margin-bottom: 24px;">
            <label style="display: block; padding: 12px; border: 2px dashed #0284c7; background: #f0f9ff; border-radius: 4px; cursor: pointer;">
                <input type="radio" name="gateway_choice" value="dummy"> 
                <strong>🛠️ Internal Sandbox / Mock Gateway</strong> (Simulate successful validation check)
            </label>
        </div>

        <button type="submit" class="btn" style="width: 100%;">Authorize Payment Transaction</button>
    </form>
</div>
{% endblock %}
