<script>
  let form = { who: '', did: '', this: '', when: '', confirmed_by: '', if_ok: '', if_doubt: '', if_not: '', status: 'pending' };
  async function register() {
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    });
    const data = await res.json();
    alert(data.status);
  }
</script>

<main>
  <label>Quem<input bind:value={form.who} /></label>
  <label>Fez<input bind:value={form.did} /></label>
  <label>O quê<input bind:value={form.this} /></label>
  <label>Quando<input bind:value={form.when} type="datetime-local" /></label>
  <label>Confirmado por<input bind:value={form.confirmed_by} /></label>
  <label>Se ok<input bind:value={form.if_ok} /></label>
  <label>Se dúvida<input bind:value={form.if_doubt} /></label>
  <label>Se não<input bind:value={form.if_not} /></label>
  <label>Status<input bind:value={form.status} /></label>
  <button on:click={register}>Registrar</button>
</main>

<style>
  main { display: flex; flex-direction: column; gap: 0.5rem; max-width: 400px; margin: auto; }
  label { display: flex; flex-direction: column; font-size: 0.9rem; }
  input, button { font-size: 1rem; }
</style>
