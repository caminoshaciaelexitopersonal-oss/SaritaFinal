'use client';
import { useForm } from 'react-hook-form';

export default function DebugPage() {
  const { register, handleSubmit } = useForm();
  const onSubmit = (data: any) => console.log(data);
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h1>Debug Form</h1>
      <input {...register('email')} placeholder="Email" />
      <button type="submit">Submit</button>
    </form>
  );
}
