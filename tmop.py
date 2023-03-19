out = (['sshpass -e scp -q -o GSSAPIAuthentication=no -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /tmp/m_elasticsearc            h.yml root@elastic-4.badcvtb40.ba.nuagenetworks.net:/etc/elasticsearch/elasticsearch.yml',
  'Restarting elasticsearch (via systemctl):  [  OK  ]',
  'Created symlink from /etc/systemd/system/multi-user.target.wants/elasticsearch.service to /usr/lib/systemd/system/elasticsea            rch.service.',
  'Done reconfiguring and restarting on elastic-4.badcvtb40.ba.nuagenetworks.net',
  'sshpass -e scp -q -o GSSAPIAuthentication=no -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /tmp/m_elasticsearc            h.yml root@elastic-5.badcvtb40.ba.nuagenetworks.net:/etc/elasticsearch/elasticsearch.yml',
  'Restarting elasticsearch (via systemctl):  [  OK  ]',
  'Created symlink from /etc/systemd/system/multi-user.target.wants/elasticsearch.service to /usr/lib/systemd/system/elasticsea            rch.service.',
  'Done reconfiguring and restarting on elastic-5.badcvtb40.ba.nuagenetworks.net',
  'sshpass -e scp -q -o GSSAPIAuthentication=no -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /tmp/m_elasticsearc            h.yml root@elastic-6.badcvtb40.ba.nuagenetworks.net:/etc/elasticsearch/elasticsearch.yml',
  'Restarting elasticsearch (via systemctl):  [  OK  ]',
  'Created symlink from /etc/systemd/system/multi-user.target.wants/elasticsearch.service to /usr/lib/systemd/system/elasticsea            rch.service.',
  'Done reconfiguring and restarting on elastic-6.badcvtb40.ba.nuagenetworks.net',
  'Waiting for checkElasticCluster ... 1 ...',
  'Waiting for checkElasticCluster ... 2 ...',
  'Done with checkElasticCluster',
  'PASSED: cluster formed.'],
 [],
 0)

print(out[0][-1])

