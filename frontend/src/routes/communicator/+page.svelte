<script>
  import { onMount } from 'svelte';
  import { chat } from '$lib/stores/chatStore.js';
  import AgentBubble from '$lib/components/AgentBubble.svelte';
  let text = '';
  let suggestions = [];

  onMount(async () => {
    const res = await fetch('/prompts');
    suggestions = await res.json();
  });

  async function send() {
    chat.update(c => [...c, { from: 'user', text }]);
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ who: 'user', did: 'said', this: text, when: new Date().toISOString(), confirmed_by: '', if_ok: '', if_doubt: '', if_not: '', status: 'pending' })
    });
    const data = await res.json();
    chat.update(c => [...c, { from: 'ia', text: data.status }]);
    text = '';
  }
</script>

<main class="chat">
  <div class="messages">
    {#each $chat as msg}
      {#if msg.from === 'ia'}
        <AgentBubble {msg} />
      {:else}
        <div class="bubble user">{msg.text}</div>
      {/if}
    {/each}
  </div>
  <input list="sug" bind:value={text} placeholder="Digite..." />
  <datalist id="sug">
    {#each suggestions as s}
      <option value={s} />
    {/each}
  </datalist>
  <button on:click={send}>Enviar</button>
</main>

<style>
  .chat { display: flex; flex-direction: column; height: 100%; }
  .messages { flex: 1; overflow: auto; }
  .bubble { padding: 0.5rem; border-radius: 8px; margin: 0.2rem; }
  .user { align-self: flex-end; background: #cee; }
</style>
