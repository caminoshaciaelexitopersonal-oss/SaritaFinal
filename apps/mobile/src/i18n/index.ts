import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  es: { translation: { "welcome": "Bienvenido a SARITA" } },
  en: { translation: { "welcome": "Welcome to SARITA" } },
  pt: { translation: { "welcome": "Bem-vindo ao SARITA" } }
};

i18n.use(initReactI18next).init({
  resources,
  lng: 'es',
  interpolation: { escapeValue: false }
});

export default i18n;
