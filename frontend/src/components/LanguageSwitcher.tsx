'use client';

import { useLocale } from 'next-intl';
import { useRouter } from 'next/navigation';
import { useTransition } from 'react';

export default function LanguageSwitcher() {
  const [isPending, startTransition] = useTransition();
  const router = useRouter();
  const localActive = useLocale();

  const onSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const nextLocale = e.target.value;
    startTransition(() => {
      router.replace(`/${nextLocale}`);
    });
  };

  return (
    <label className='relative text-gray-400'>
      <select
        defaultValue={localActive}
        className='inline-flex appearance-none bg-transparent py-3 pl-2 pr-6'
        onChange={onSelectChange}
        disabled={isPending}
      >
        <option value='es'>Español</option>
        <option value='en'>English</option>
      </select>
    </label>
  );
}