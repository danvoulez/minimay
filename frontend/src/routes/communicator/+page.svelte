<script>
  import { messages } from '$lib/stores.js';
  import { onMount } from 'svelte';
  let text = '';
  let suggestions = [];

  onMount(async () => {
    const res = await fetch('/prompts');
    suggestions = await res.json();
  });

  async function send() {
    messages.update(m => [...m, { author: 'eu', text }]);
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ this: text, who: 'eu', did: 'said', when: new Date().toISOString(), confirmed_by: '', if_ok: '', if_doubt: '', if_not: '', status: 'pending' })
    });
    const data = await res.json();
    messages.update(m => [...m, { author: 'IA', text: data.status }]);
    text = '';
  }
</script>

<div class="chat">
  <div class="messages">
    {#each $messages as msg}
      <div class="bubble {msg.author}">{msg.text}</div>
    {/each}
  </div>
  <div class="input-area">
    <input list="sug" bind:value={text} placeholder="mensagem" />
    <datalist id="sug">
      {#each suggestions as s}
        <option value={s} />
      {/each}
    </datalist>
    <button on:click={send}>Enviar</button>
  </div>
</div>

<style>
  .chat { display: flex; flex-direction: column; height: 100%; }
  .messages { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 0.25rem; }
  .bubble { padding: 0.5rem; border-radius: 6px; max-width: 70%; }
  .bubble.eu { background: #dcf8c6; align-self: flex-end; }
  .bubble.IA { background: #eee; align-self: flex-start; }
  .input-area { display: flex; gap: 0.5rem; }
  input { flex: 1; }
</style>
