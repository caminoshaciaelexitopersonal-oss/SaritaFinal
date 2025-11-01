import 'module-alias/register';
import type { NextConfig } from "next";
import createNextIntlPlugin from 'next-intl/plugin';
import path from "path";

const withNextIntl = createNextIntlPlugin('src/i18n.ts');

const nextConfig: NextConfig = {
  webpack: (config) => {
    config.resolve.alias['@'] = path.resolve(__dirname, "src");
    return config;
  },
  images: {
    remotePatterns: [
      {
        protocol: 'http',
        hostname: 'localhost',
        port: '8000',
        pathname: '/media/**',
      },
      {
        protocol: 'http',
        hostname: '127.0.0.1',
        port: '8000',
        pathname: '/media/**',
      },
    ],
  },
};

export default withNextIntl(nextConfig);
