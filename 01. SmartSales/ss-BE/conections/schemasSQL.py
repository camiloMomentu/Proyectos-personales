schemas = {
    'users':"""
            INSERT 
                INTO users(first_name, last_name, email, password, is_admin, is_active, created_at, company_id) 
            VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s)
    """,

    'companies':"""
            INSERT 
                INTO companies(name, is_active, create_at) 
            VALUES
                (%s,%s,%s)
    """
}

