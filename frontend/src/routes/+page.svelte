<script>
  import { onMount } from 'svelte';
  let text = '';
  let feedback = '';
  let suggestions = [];

  onMount(async () => {
    const res = await fetch('/prompts');
    suggestions = await res.json();
  });

  async function register() {
    feedback = 'Enviando...';
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ this: text, who: 'user', did: 'report', when: new Date().toISOString(), confirmed_by: '', if_ok: '', if_doubt: '', if_not: '', status: 'pending' })
    });
    const data = await res.json();
    feedback = data.status;
    text = '';
  }
</script>

<main>
  <input list="sug" bind:value={text} placeholder="o que aconteceu?" />
  <datalist id="sug">
    {#each suggestions as sug}
      <option value={sug} />
    {/each}
  </datalist>
  <button on:click={register}>Registrar</button>
  {#if feedback}
    <p>{feedback}</p>
  {/if}
</main>

<style>
  main { display: flex; flex-direction: column; gap: 0.5rem; max-width: 400px; margin: auto; }
  input, button { font-size: 1.2rem; }
</style>
