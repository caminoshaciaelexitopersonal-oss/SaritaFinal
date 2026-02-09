import os

base_path = 'backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios'

for domain in os.listdir(base_path):
    domain_path = os.path.join(base_path, domain)
    if os.path.isdir(domain_path):
        coronel_file = os.path.join(domain_path, 'coronel.py')
        if os.path.exists(coronel_file):
            with open(coronel_file, 'r') as f:
                content = f.read()

            # Change ...prestadores.capitanes.gestion_comercial to ...capitanes
            new_content = content.replace('...prestadores.capitanes.gestion_comercial.', '...capitanes.')

            if new_content != content:
                print(f"Fixed imports in {coronel_file}")
                with open(coronel_file, 'w') as f:
                    f.write(new_content)
