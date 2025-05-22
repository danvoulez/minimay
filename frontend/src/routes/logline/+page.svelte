<script>
  import { onMount } from 'svelte';
  import { selectedLog } from '$lib/stores.js';
  let text = '';
  let feedback = '';
  let suggestions = [];
  let logs = [];

  onMount(async () => {
    const p = await fetch('/prompts');
    suggestions = await p.json();
    const res = await fetch('/timeline');
    if (res.ok) logs = await res.json();
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
    if (res.ok) {
      logs.push({ this: text, who: 'user', did: 'report' });
    }
  }
</script>

<div class="logline">
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

  {#if logs.length}
    <ul class="timeline">
      {#each logs as log}
        <li on:click={() => selectedLog.set(log)}>{log.who}: {log.did} {log.this}</li>
      {/each}
    </ul>
  {/if}
</div>

<style>
  .logline { display: flex; flex-direction: column; gap: 0.5rem; max-width: 400px; margin: auto; }
  input, button { font-size: 1.2rem; }
  .timeline { list-style: none; padding-left: 0; }
  .timeline li { cursor: pointer; padding: 0.25rem 0; }
</style>
