import React, { useState, useEffect } from 'react';
import { TreeView, Button, Modal, Input, Select } from '../../components/ui';
import { accountingService } from './accountingService';

export const ChartOfAccounts = () => {
  const [cuentas, setCuentas] = useState([]);
  const [selected, setSelected] = useState(null);
  const [modal, setModal] = useState(false);
  const [form, setForm] = useState({ code: '', name: '', parent: '', type: 'asset' });

  useEffect(() => {
    fetchCuentas();
  }, []);

  const fetchCuentas = async () => {
    const data = await accountingService.getCuentasTree();
    setCuentas(data);
  };

  const handleEdit = (cuenta) => {
    setForm(cuenta);
    setModal(true);
  };

  const handleCreate = () => {
    setForm({ code: '', name: '', parent: '', type: 'asset' });
    setModal(true);
  };

  const handleDelete = async (id) => {
    await accountingService.deleteCuenta(id);
    fetchCuentas();
  };

  const handleSave = async () => {
    if (form.id) {
      await accountingService.updateCuenta(form.id, form);
    } else {
      await accountingService.createCuenta(form);
    }
    setModal(false);
    fetchCuentas();
  };

  return (
    <div>
      <div className="flex justify-between mb-6">
        <h2>Catálogo PUC Mi Negocio</h2>
        <Button onClick={handleCreate}>Nueva Cuenta</Button>
      </div>
      <TreeView data={cuentas} onSelect={handleEdit}>
        {(node) => (
          <div className="flex justify-between">
            <span>{node.code} - {node.name}</span>
            <div>
              <Button size="sm" onClick={() => handleEdit(node)}>Edit</Button>
              <Button size="sm" variant="destructive" onClick={() => handleDelete(node.id)}>Delete</Button>
            </div>
          </div>
        )}
      </TreeView>
      <Modal open={modal} onClose={() => setModal(false)}>
        <Input placeholder="Código 6 dígitos" value={form.code} onChange={(e) => setForm({...form, code: e})} />
        <Input placeholder="Nombre" value={form.name} onChange={(e) => setForm({...form, name: e})} />
        <Select value={form.type} onChange={(t) => setForm({...form, type: t})}>
          <option>asset</option>
          <option>liability</option>
        </Select>
        <Button onClick={handleSave}>Guardar</Button>
      </Modal>
    </div>
  );
};

